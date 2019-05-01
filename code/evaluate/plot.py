import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from util.util import loadConfig, loadBinary, loadJsonFromFile, convertCfmAbsToPerc
from train.mlp import getConfusionMatrix, plotConfusionMatrix
from tensorflow.python.keras import models
from matplotlib.pyplot import savefig
import numpy as np
import argparse

parser = argparse.ArgumentParser(
    description='Plot evaluations for a trained model.'
)

parser.add_argument('--config',
        required    = True,
        help        ="File with the configuration for the training run")


args = parser.parse_args()

config = loadConfig(args.config)

model_file = os.path.join(config["processedDataDir"], "train", "mlp_model.h5")
print("Loading model: {}".format(model_file))
model = models.load_model(model_file)

(test_texts, test_labels) = loadJsonFromFile(config, "test.json", "train")

cfm = getConfusionMatrix(config, model, test_texts, test_labels)
perCfm = convertCfmAbsToPerc(cfm)
plotConfusionMatrix(config, perCfm)
savefig(os.path.join(config["processedDataDir"], "evaluate", "cfm.png"))
