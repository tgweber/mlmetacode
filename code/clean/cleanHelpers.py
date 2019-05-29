import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import ijson
import json
import re
import util.util as util
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
from cleanSchemeHelpers import *

def registerMapping(anzsrc, payload, anzsrc2subject):
    if anzsrc not in anzsrc2subject.keys():
        anzsrc2subject[anzsrc] = { payload: 1, "total": 1}
    elif payload not in anzsrc2subject[anzsrc].keys():
        anzsrc2subject[anzsrc][payload] = 1
        anzsrc2subject[anzsrc]["total"] += 1
    else:
        anzsrc2subject[anzsrc][payload] += 1
        anzsrc2subject[anzsrc]["total"] += 1

def getBaseAnzsrc(config, subject):
    payload = subject["value"].lower().strip()
    for scheme in config["clean"]["schemes"]:
        isScheme = getSchemeTester(scheme)
        if isScheme and isScheme(config, subject):
            return getAnzsrcFromScheme(scheme, config, subject)
    return None

def getMinLength(config, field):
    return config["clean"]["minLength"].get(field, 1)

def getPayload(config, document):
    payload= {}
    for field in config["clean"]["dmode"].split("_"):
        fieldPlural = field + "s"
        payloadPart = ""
        if fieldPlural not in document.keys():
            continue
        for instance in document[fieldPlural]:
            if not instance["value"]:
                continue
            try:
                if not detect(instance["value"]) == "en":
                    continue
            except LangDetectException as e:
                continue
            payloadPart += " " + instance["value"]
        if len(payloadPart.split()) < getMinLength(config, field):
            continue
        payload[field] = payloadPart
    return payload

def isSpecialChunk(config, fileName):
    if config["regex"]["special"].match(os.path.basename(fileName)):
        return True
    return False

def getLabels(config, document, result, fileName):
    seenSchemeURIs = []
    seenSubjectSchemes = []
    labels = set()

    if isSpecialChunk(config, fileName):
        lookup = os.path.basename(fileName)
        label = config["specialDict"][lookup]
        labels.add(label)
    else:
        for subject in document["subjects"]:
            # count the documents with this schemeURI (once)
            if "schemeURI" in subject.keys():
                schemeURI = subject["schemeURI"]
                if schemeURI not in seenSchemeURIs:
                    seenSchemeURIs.append(schemeURI)
                    result["schemeURIs"][schemeURI] = (
                        result["schemeURIs"].get(schemeURI, 0) + 1)
            # count the documents with this subjectScheme (once)
            if "subjectScheme" in subject.keys():
                subjectScheme = subject["subjectScheme"]
                if subjectScheme not in seenSchemeURIs:
                    seenSchemeURIs.append(subjectScheme)
                    result["subjectSchemes"][subjectScheme] = (
                        result["subjectSchemes"].get(subjectScheme, 0) + 1)
            # add to label if fitting
            anzsrc = getBaseAnzsrc(config, subject)
            if not anzsrc:
                continue

            registerMapping(anzsrc,
                            subject["value"],
                            result["anzsrc2subject"])
            labels.add(anzsrc[:2].strip())
    return labels

def init_result(config):
    result = {
        "documents" : 0,
        "notAnnotatable": 0,
        "multiAnnotations": 0,
        "payloadNotFit": 0,
        "useableDocuments": 0,
        "duplicates": 0,
        "schemeURIs" : {},
        "special" : {},
        "subjectSchemes" : {},
        "anzsrc2subject" : {},
        "payload" : {},
    }

    for label in config["labels"]:
        result["anzsrc2subject"][label] = {"total": 0}
        result["special"][label] = 0
        result["payload"][label] = {}

    return result

def mergeSubjectInfo2Result(result, subjectInfo):
    for key in subjectInfo.keys():
        if key == "anzsrc2subject":
            result[key] = result.get(key, {})
            for anzsrc, anzsrcValues in subjectInfo[key].items():
                if anzsrc not in result[key].keys():
                    result[key][anzsrc] = { "total": 0}
                for mapped, count in anzsrcValues.items():
                    result[key][anzsrc][mapped] = result[key][anzsrc].get(mapped, 0) + count
                    result[key][anzsrc]["total"] += count
        else:
            for entry, value in subjectInfo[key].items():
                result[key][entry] = result[key].get(entry, 0) + value


def processFile(instruction):
    config = instruction[0]
    fileName = instruction[1]
    config["logger"].info("  Processing: {}".format(fileName))
    cleanId = config["regex"]["dataInput"].match(fileName).group(1)
    resultFile = os.path.join(
        config["clean"]["outputDir"],
        cleanId + ".chunk.json"
    )
    if os.path.isfile(resultFile):
        config["logger"].info("    {} already processed: {}".format(
            os.path.basename(fileName),
            resultFile
        ))
        return True
    try:
        with open(fileName) as f:
            result = init_result(config)
            for document in ijson.items(f, 'documents.item'):
                result["documents"] += 1
                subjectInfo = {
                    "schemeURIs": {},
                    "subjectSchemes": {},
                    "anzsrc2subject": {}
                }
                labels = getLabels(config, document, subjectInfo, fileName)

                mergeSubjectInfo2Result(
                    result, {
                        "subjectSchemes": subjectInfo["subjectSchemes"],
                        "schemeURIs": subjectInfo["schemeURIs"]
                    }
                )

                if not labels:
                    result["notAnnotatable"] += 1
                    continue
                if len(labels) != 1:
                    result["multiAnnotations"] += 1
                    continue

                label = labels.pop()
                payload = getPayload(config, document)

                if not len(payload) == len(config["clean"]["dmode"].split("_")):
                    result["payloadNotFit"] += 1
                    continue
                payloadHash = util.getDictHash(payload)
                if payloadHash in result["payload"][label].keys():
                    result["duplicates"] += 1
                result["payload"][label][payloadHash] = payload
                mergeSubjectInfo2Result(
                    result, { "anzsrc2subject": subjectInfo["anzsrc2subject"] }
                )
                if isSpecialChunk(config, fileName):
                    result["special"][label] += 1
        config["logger"].info("    Save results for: {}".format(resultFile))
        with open(resultFile, "w") as f:
            json.dump(result, f)
        return True
    except Exception as e:
        config["logger"].error(
            "Failure in processing file {}: {} {} {} {}".format(
                fileName,
                sys.exc_info()[-1].tb_lineno,
                e.__class__,
                e.__doc__,
                e
            )
        )
        raise