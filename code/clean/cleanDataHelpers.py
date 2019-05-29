import re
# used to check the subject[subjectScheme] payload to determine whether this is
# a dewey decimal subject
ddcNames = [
        "DDC",
        "ddc",
        "dewey",
        "DeweyDecimalClassification",
        "ddccode",
        "Dewey Classification"
            " (http://opac.bncf.firenze.sbn.it/opac/controller.jsp"
            "?action=dewey_browse&deweypath_cod=9)",
        "Dewey decimal Classification",
        "ddc-dbn",
        "eterms:DDC"
]

# Used to map the payload (subject["value"]) of a DDC-subject to the base classes
# of ANZSRC. Unhandled DDC classes:
#  ^03[^.] | Encyclopedias & books of facts
#  ^04[^.] | Unassigned (formerly Biographies)
#  ^05[^.] | Magazines, journals & serials
#  ^06[^.] | Associations, organizations & museums
#  ^08[^.] | Quotations
#  ^09[^.] | Manuscripts & rare books
#  ^35[^.] | Public administration & military science
#  ^39[^.] | Customs, etiquette, & folklore
#  ^50[^.] | Science (too specific, subcategories are partly handled)
#  ^64[^.] | Home & family management
#  ^79[^.] | Sports, games & entertainment
#  ^91[^.] | Geography & travel
#  ^92[^.] | Biography & genealogy

# ! order matters: first come first serve, rearranging might result in false
# positives

Ddc2Anszrc = [
        [ 5, # 5, #"05 environmental sciences",
            re.compile(
                '^57[7-9].*'
                '|ddc 57[7-8]'
            )
        ],
        [ 4, # 4, #"04 earth sciences",
            re.compile(
                '^55[^.]+.*'
                '|^56[^.]+.*'
                '|^ddc 55[^.]+.*'
                '|^ddc 56[^.]+.*'
                '|.*earth sciences and geology$'
                '|.*550\s*\|\s*geowissenschaften.*'
                '|^912$'
                '|geowissenschaften$'
            )
        ],
        [ 11, # 11, #"11 medical and health sciences",
            re.compile(
                '^61[^.]+.*'
                '|^ddc 61[^.]+.*'
                '|^medizin und gesundheit'
                )
        ],
        [ 6, # 6, #"06 biological sciences",
            re.compile(
                '^57[^.]+.*'
                '|^58[^.]+.*'
                '|^59[^.]+.*'
                '|^ddc 57[^.]+.*'
                '|^ddc 58[^.]+.*'
                '|^ddc 59[^.]+.*'
                '|.*naturwissenschaften::570.*'
                '|.*naturwissenschaften::580.*'
                '|.*naturwissenschaften::590.*'
                '|biology'
                )
        ],
        [ 8, # 8, #"08 information and computing sciences",
            re.compile(
                '^00[^.]+.*'
                '|^01[^.]+.*'
                '|^02[^.]+.*'
                '|^ddc 00[^.]+.*'
                '|^ddc 01[^.]+.*'
                '|^ddc 02[^.]+.*'
                '|.*allgemeines, wissenschaft::000.*$'
                '|^bibliotheks- und informationswissenschaften$'
                )
        ],
        [ 14, # 14, #"14 economics",
            re.compile(
                '^33[^.]+.*'
                '|^ddc 33[^.]+.*'
                '|^wirtschaft$'
                )
        ],
        [ 9, # 9, #"09 engineering",
                re.compile(
                    '^62[^.]+.*'
                    '|^66[^.]+.*'
                    '|^67[^.]+.*'
                    '|^68[^.]+.*'
                    '|^ddc 62[^.]+.*'
                    '|^ddc 66[^.]+.*'
                    '|^ddc 67[^.]+.*'
                    '|^ddc 68[^.]+.*'
                    )
        ],
        [ 2, # 2, #"02 physical science",
            re.compile(
                '^52[^.]+.*'
                '|^53[^.]+.*'
                '|^ddc 52[^.]+.*'
                '|^ddc 53[^.]+.*'
                '|.*530 \| physik.*'
                )
        ],
        [ 21, # 21, #"21 history and archaeology",
                re.compile(
                    '^90[^.]+.*'
                    '|^93[^.]+.*'
                    '|^94[^.]+.*'
                    '|^95[^.]+.*'
                    '|^96[^.]+.*'
                    '|^97[^.]+.*'
                    '|^98[^.]+.*'
                    '|^99[^.]+.*'
                    '|^ddc 90[^.]+.*'
                    '|^ddc 93[^.]+.*'
                    '|^ddc 94[^.]+.*'
                    '|^ddc 95[^.]+.*'
                    '|^ddc 96[^.]+.*'
                    '|^ddc 97[^.]+.*'
                    '|^ddc 98[^.]+.*'
                    '|^ddc 99[^.]+.*'
                    '|^271.*'
                    )
        ],
        [ 3, # 3, #"03 chemical science",
                re.compile(
                    '^54[^.]+.*'
                    '|^54[^.]+.*'
                    '|.*540 \| chemie.*'
                    )
        ],
        [ 20, # 20, #"20 language, communication and culture",
                re.compile(
                    '^4\d+[^.]+.*'
                    '|^8\d+[^.-]+.*'
                    '|^306.*'
                    '|^ddc 4[^.]+.*'
                    '|^ddc 8[^.]+.*'
                    '|^ddc 306.*'
                    '|^8 language\. linguistics\. literature$'
                    '|^81 linguistics and languages'
                    '|.*dewey decimal classification::400 \| sprache, linguistik.*$'
                    '|.*dewey decimal classification::800 \| literatur, rhetorik, literaturwissenschaft.*$'
                    )
        ],
        [ 16, # 16, #"16 studies in human society",
                re.compile(
                    '^30[^.]+.*'
                    '|^32[^.]+.*'
                    '|^36[^.]+.*'
                    '|^ddc 30[^.]+.*'
                    '|^ddc 32[^.]+.*'
                    '|^ddc 36[^.]+.*'
                    '|.*sozialwissenschaften, soziologie, anthropologie::330$'
                    '|.*sozialwissenschaften, soziologie, anthropologie::330.*'
                    '|.*sozialwissenschaften, soziologie, anthropologie::360.*'
                    '|^soziale probleme und sozialdienste; verbände$'
                    '|^0 social sciences'
                    '|^3 social sciences$'
                    '|^sozialwissenschaften$'
                    )
        ],
        [ 7, # 7, #"07 agricultural and veterinary science",
                re.compile(
                    '^63[^.]+.*'
                    '|^ddc 63[^.]+.*'
                    '|^landwirtschaft und verwandte bereiche$'
                    '|.*technik::630.*'
                    )
        ],
        [ 17, # 17, #"17 psychology and cognitive sciences",
                re.compile(
                    '^15[^.]+.*'
                    '|^ddc 15[^.]+.*'
                    '|^psychologie$'
                    )
        ],
        [ 10, # 10, #"10 technology",
                re.compile(
                    '^60[^.]+.*'
                    '|^ddc 60[^.]+.*'
                    )
        ],
        [ 13, # 13, #"13 education",
                re.compile(
                    '^37[^.]+.*'
                    '^507.*'
                    '|^ddc 37[^.]+.*'
                    '|^ddc 507.*'
                    '|.*sozialwissenschaften, soziologie, anthropologie::370.*'
                    )
        ],
        [ 1, # 1, #"01 mathematical science",
                re.compile(
                    '^31\d+.*'
                    '|^51[^.]+.*'
                    '|^ddc 31[^.]+.*'
                    '|^ddc 51[^.]+.*'
                    '|.*510 \| mathematik.*'
                    )
        ],
        [ 18, # 18, #"18 law and legal studies",
                re.compile(
                    '^34[^.]+.*'
                    '|^ddc 34[^.]+.*'
                    '|.*sozialwissenschaften, soziologie, anthropologie::340.*'
                    '|^recht$'
                    )
        ],
        [ 22, # 22, #"22 philosophy and religious studies",
                re.compile(
                    '^(1|2)\d+.*'
                    '|^507.*'
                    '|^ddc (1|2)[^.]+.*'
                    '|^ddc 507.*'

                    )
        ],
        [ 19, # 19, #"19 studies in creative arts and writing",
                re.compile(
                    '^07[^.]+.*'
                    '|^70[^.]+.*'
                    '|^73[^.]+.*'
                    '|^74[^.]+.*'
                    '|^75[^.]+.*'
                    '|^76[^.]+.*'
                    '|^77[^.]+.*'
                    '|^78[^.]+.*'
                    '|^ddc 07[^.]+.*'
                    '|^ddc 70[^.]+.*'
                    '|^ddc 73[^.]+.*'
                    '|^ddc 74[^.]+.*'
                    '|^ddc 75[^.]+.*'
                    '|^ddc 76[^.]+.*'
                    '|^ddc 77[^.]+.*'
                    '|^ddc 78[^.]+.*'
                    )
        ],
        [ 15, # 15, #"15 commerce, management, tourism and services",
                re.compile(
                    '^38[^.]+.*'
                    '|^65[^.].*'
                    '|^ddc 38[^.]+.*'
                    '|^ddc 65[^.]+.*'
                    '|.*sozialwissenschaften, soziologie, anthropologie::380.*'
                    )
        ],
        [ 12, # 12, #"12 built environment and design",
                re.compile(
                    '^69[^.*]'
                    '|^71[^.*]'
                    '|^72[^.*]'
                    '|^ddc 69[^.]+.*'
                    '|^ddc 71[^.]+.*'
                    '|^ddc 72[^.]+.*'
                    )
        ]
]

# ORDER MATTERS
narcis2Anzsrc = [
        [ 5, #"05 environmental sciences",
            re.compile(
                'http://www.narcis.nl/classfication/D224\d{2}'
            )
        ],
        [ 4, #"04 earth sciences",
            re.compile(
                'http://www.narcis.nl/classfication/D15\d{3}'
            )
        ],
        [ 11, #"11 medical and health sciences",
            re.compile(
                'http://www.narcis.nl/classfication/D2(3|4)\d{3}'
                )
        ],
        [ 6, #"06 biological sciences",
            re.compile(
                'http://www.narcis.nl/classfication/D22\d{3}'
                )
        ],
        [ 8, #"08 information and computing sciences",
            re.compile(
                'http://www.narcis.nl/classfication/D16\d{3}'
                )
        ],
        [ 14, #"14 economics",
            re.compile(
                'http://www.narcis.nl/classfication/D70\d{3}'
                )
        ],
        [ 9, #"09 engineering",
            re.compile(
                'http://www.narcis.nl/classfication/(D14310|D14220|D1443\d{1}|D1444\d{1}|D146\d{2})'
                )
        ],
        [ 2, #"02 physical science",
            re.compile(
                'http://www.narcis.nl/classfication/(D12\d{3}|D17\d{3})'
                )
        ],
        [ 21, #"21 history and archaeology",
                re.compile(
                'http://www.narcis.nl/classfication/(D34\d{3}|D37\d{3})'
                    )
        ],
        [ 3, #"03 chemical science",
                re.compile(
                'http://www.narcis.nl/classfication/D13\d{3}'
                    )
        ],
        [ 20, #"20 language, communication and culture",
                re.compile(
                'http://www.narcis.nl/classfication/(D36\d{3}|D63\d{3}|D66\d{3})'
                    )
        ],
        [ 16, #"16 studies in human society",
                re.compile(
                'http://www.narcis.nl/classfication/(D6(0|1|8|9)\d{3}|D42\d{3})'
                    )
        ],
        [ 7, #"07 agricultural and veterinary science",
                re.compile(
                'http://www.narcis.nl/classfication/(D18\d{3}|D26\d{3})'
                    )
        ],
        [ 17, #"17 psychology and cognitive sciences",
                re.compile(
                'http://www.narcis.nl/classfication/(D51\d{3})'
                    )
        ],
        [ 10, #"10 technology",
                re.compile(
                'http://www.narcis.nl/classfication/(E16\d{3}|D141\d{2}|D142(1|3|4)\d{1}|D143(1|2)\d{1}|D145\d{2}|D14(7|8|9)\d{2})'

                    )
        ],
        [ 13, #"13 education",
                re.compile(
                'http://www.narcis.nl/classfication/(D52\d{3})'
                    )
        ],
        [ 1, #"01 mathematical science",
                re.compile(
                'http://www.narcis.nl/classfication/(D11\d{3})'
                    )
        ],
        [ 18, #"18 law and legal studies",
                re.compile(
                'http://www.narcis.nl/classfication/(D41\d{3})'
                    )
        ],
        [ 22, #"22 philosophy and religious studies",
                re.compile(
                'http://www.narcis.nl/classfication/(D3(2|3)\d{3})'
                    )
        ],
        [ 19, #"19 studies in creative arts and writing",
                re.compile(
                'http://www.narcis.nl/classfication/(D35(1|2|3)\d{2})'
                    )
        ],
        [ 12, #"12 built environment and design",
                re.compile(
                'http://www.narcis.nl/classfication/(D355\d{2}|D147\d{2})'
                    )
        ]
]
# ORDER IS IRRELEVANT
bk2Anzsrc = [
        [ 1, #"01 mathematical science"
         re.compile( '^31.*') ],
        [ 2, #"02 physical science",
         re.compile( '^(33|39).*') ],
        [ 3, #"03 chemical science",
         re.compile( '^35.*') ],
        [ 4, #"04 earth sciences",
         re.compile( '^38.*') ],
        [ 6, #"06 biological sciences",
         re.compile( '^42.*') ],
        [ 7, #"07 agricultural and veterinary science",
         re.compile( '^(46|48).*') ],
        [ 8, #"08 information and computing sciences",
         re.compile( '^54.*') ],
        [ 9, #"09 engineering",
         re.compile( '^(51|52|53).*') ],
        [ 10, #"10 technology",
         re.compile( '^(50|58).*') ],
        [ 11, #"11 medical and health sciences",
         re.compile( '^44.*') ],
        [ 12, #"12 built environment and design",
         re.compile( '^56.*') ],
        [ 13, #"13 education",
         re.compile( '^(80|81).*') ],
        [ 14, #"14 economics",
         re.compile( '^8(3|5).*') ],
        [ 16, #"16 studies in human society",
         re.compile( '^(71|89).*') ],
        [ 17, #"17 psychology and cognitive sciences",
         re.compile( '^77.*') ],
        [ 18, #"18 law and legal studies",
         re.compile( '^86.*') ],
        [ 19, #"19 studies in creative arts and writing",
         re.compile( '^(20|21|24).*') ],
        [ 20, #"20 language, communication and culture",
         re.compile( '^(05|17|18|73).*') ],
        [ 21, #"21 history and archaeology",
         re.compile( '^15.*') ],
        [ 22, #"22 philosophy and religious studies",
         re.compile( '^(08|11).*') ]
]

# ORDER IS IRRELEVANT
linsearch2Anzsrc = [
        [ 1, #"01 mathematical science"
          re.compile( '^Mathematics$') ],
        [ 2, #"02 physical science"
          re.compile( '^Physics$') ],
        [ 3, #"03 chemical science"
          re.compile( '^Chemistry$') ],
        [ 4, #"04 earth sciences"
          re.compile( '^Earth Science$')],
        [ 6, #"06 biological sciences"
          re.compile( '^Biology$') ],
        [ 7, #"07 agricultural and veterinary science"
          re.compile( '^Horticulture$') ],
        [ 8, #"08 information and computing sciences"
          re.compile( '^Computer Science$') ],
        [ 9, #"09 engineering"
          re.compile( '^Engineering$') ],
        [ 12, #"12 built environment and design"
          re.compile( '^Architecture') ],
        [ 13, #"13 education"
          re.compile( 'Educational Science') ],
        [ 14, #"14 economics"
          re.compile( 'Economics') ],
        [ 18, #"18 law and legal studies"
          re.compile( '^Law$') ],
        [ 20, #"20 language, communication and culture"
          re.compile( '^Lingustics$') ],
        [ 21, #"21 history and archaeology"
          re.compile( '^History$') ],
        [ 22, #"22 philosophy and religious studies"
          re.compile( '^(Philosophy|Theology)$') ]
]

bepress2Anzsrc = [
        [ 1, #"01 mathematical science",
            re.compile(

Applied Mathematics
Applied Mathematics: Control Theory
Applied Mathematics: Dynamic Systems
Applied Mathematics: Non-linear Dynamics
Applied Mathematics: Numerical Analysis and Computation
Applied Mathematics: Ordinary Differential Equations and Applied Dynamics
Applied Mathematics: Partial Differential Equations
Applied Mathematics: Special Functions
Applied Mathematics: Other Applied Mathematics
Mathematics
Mathematics: Algebra
Mathematics: Algebraic Geometry
Mathematics: Analysis
Mathematics: Discrete Mathematics and Combinatorics
Mathematics: Dynamical Systems
Mathematics: Geometry and Topology
Mathematics: Harmonic Analysis and Representation
Mathematics: Logic and Foundations
Mathematics: Number Theory
Mathematics: Set Theory
Mathematics: Other Mathematics
Statistics and Probability
Statistics and Probability: Applied Statistics
Statistics and Probability: Biometry
Statistics and Probability: Biostatistics
Statistics and Probability: Categorical Data Analysis
Statistics and Probability: Clinical Trials
Statistics and Probability: Design of Experiments and Sample Surveys
Statistics and Probability: Institutional and Historical
Statistics and Probability: Longitudinal Data Analysis and Time Series
Statistics and Probability: Microarrays
Statistics and Probability: Multivariate Analysis
Statistics and Probability: Probability
Statistics and Probability: Statistical Methodology
Statistics and Probability: Statistical Models
Statistics and Probability: Statistical Theory
Statistics and Probability: Survival Analysis
Statistics and Probability: Vital and Health Statistics
Statistics and Probability: Other Statistics and Probability
            )
        ],
        [ 2, #"02 physical science",
            re.compile(

Astrophysics and Astronomy
Astrophysics and Astronomy: Cosmology, Relativity, and Gravity
Astrophysics and Astronomy: External Galaxies
Astrophysics and Astronomy: Instrumentation
Astrophysics and Astronomy: Physical Processes
Astrophysics and Astronomy: Stars, Interstellar Medium and the Galaxy
Astrophysics and Astronomy: The Sun and the Solar System
Astrophysics and Astronomy: Other Astrophysics and Astronomy
Physics
Physics: Atomic, Molecular and Optical Physics
Physics: Biological and Chemical Physics
Physics: Condensed Matter Physics
Physics: Elementary Particles and Fields and String Theory
Physics: Engineering Physics
Physics: Fluid Dynamics
Physics: Nuclear
Physics: Optics
Physics: Plasma and Beam Physics
Physics: Quantum Physics
Physics: Statistical, Nonlinear, and Soft Matter Physics
Physics: Other Physics
            )
        ],
        [ 3, #"03 chemical science",
            re.compile(

Chemistry
Chemistry: Analytical Chemistry
Chemistry: Environmental Chemistry
Chemistry: Inorganic Chemistry
Chemistry: Materials Chemistry
Chemistry: Medicinal-Pharmaceutical Chemistry
Chemistry: Organic Chemistry
Chemistry: Physical Chemistry
Chemistry: Polymer Chemistry
Chemistry: Radiochemistry
Chemistry: Other Chemistry
            )
        ],
        [ 4, #"04 earth sciences",
            re.compile(

Earth Sciences
Earth Sciences: Biogeochemistry
Earth Sciences: Cosmochemistry
Earth Sciences: Geochemistry
Earth Sciences: Geology
Earth Sciences: Geomorphology
Earth Sciences: Geophysics and Seismology
Earth Sciences: Glaciology
Earth Sciences: Hydrology
Earth Sciences: Mineral Physics
Earth Sciences: Paleobiology
Earth Sciences: Paleontology
Earth Sciences: Sedimentology
Earth Sciences: Soil Science
Earth Sciences: Speleology
Earth Sciences: Stratigraphy
Earth Sciences: Tectonics and Structure
Earth Sciences: Volcanology
Earth Sciences: Other Earth Sciences
            )
        ],
        [ 5, #"05 environmental sciences",
            re.compile(
Environmental Sciences
Environmental Sciences: Environmental Education
Environmental Sciences: Environmental Health and Protection
Environmental Sciences: Environmental Indicators and Impact Assessment
Environmental Sciences: Environmental Monitoring
Environmental Sciences: Natural Resource Economics
Environmental Sciences: Natural Resources and Conservation
Environmental Sciences: Natural Resources Management and Policy
Environmental Sciences: Oil, Gas, and Energy
Environmental Sciences: Sustainability
Environmental Sciences: Water Resource Management
Environmental Sciences: Other Environmental Sciences
Oceanography and Atmospheric Sciences and Meteorology
Oceanography and Atmospheric Sciences and Meteorology: Atmospheric Sciences
Oceanography and Atmospheric Sciences and Meteorology: Climate
Oceanography and Atmospheric Sciences and Meteorology: Fresh Water Studies
Oceanography and Atmospheric Sciences and Meteorology: Meteorology
Oceanography and Atmospheric Sciences and Meteorology: Oceanography
Oceanography and Atmospheric Sciences and Meteorology: Other Oceanography and Atmospheric Sciences and Meteorology
            )
        ],
        [ 6, #"06 biological sciences",
            re.compile(
             '^Ecology and Evolutionary Biology$'
             '|^Behavior and Ethology$'
             '|^Desert Ecology$'
             '|^Evolution$'
             '|^Population Biology$'
             '|^Terrestrial and Aquatic Ecology$'
             '|^Other Ecology and Evolutionary Biology$'
             '|^Biochemistry, Biophysics, and Structural Biology$'
             '|^Biochemistry$'
             '|^Biophysics$'
             '|^Molecular Biology$'
             '|^Structural Biology$'
             '|^Other Biochemistry, Biophysics, and Structural Biology$'
             '|^Biodiversity$'
             '|^Biology$'
             '|^Biology: Integrative Biology$'
             '|^Cell and Developmental Biology$'
             '|^Cancer Biology$'
             '|^Cell Anatomy$'
             '|^Cell Biology$'
             '|^Developmental Biology$'
             '|^Other Cell and Developmental Biology$'
             '|^Genetics and Genomics$'
             '|^Computational Biology$'
             '|^Genetics$'
             '|^Genomics$'
             '|^Molecular Genetics$'
             '|^Other Genetics and Genomics$'
             '|^Laboratory and Basic Science Research$'
             '|^Marine Biology$'
             '|^Microbiology$'
             '|^Bacteriology$'
             '|^Environmental Microbiology and Microbial Ecology$'
             '|^Microbial Physiology$'
             '|^Organismal Biological Physiology$'
             '|^Pathogenic Microbiology$'
             '|^Virology$'
             '|^Other Microbiology$'
             '|^Neuroscience and Neurobiology$'
             '|^Behavioral Neurobiology$'
             '|^Cognitive Neuroscience$'
             '|^Computational Neuroscience$'
             '|^Developmental Neuroscience$'
             '|^Molecular and Cellular Neuroscience$'
             '|^Systems Neuroscience$'
             '|^Other Neuroscience and Neurobiology$'
             '|^Physiology$'
             '|^Cellular and Molecular Physiology$'
             '|^Comparative and Evolutionary Physiology$'
             '|^Endocrinology$'
             '|^Exercise Physiology$'
             '|^Systems and Integrative Physiology$'
             '|^Other Physiology$'
             '|^Botany$'
             '|^Bryology$'
             '|^Plant Biology$'
             '|^Plant Breeding and Genetics$'
             '|^Plant Pathology$'
             '|^Weed Science$'
             '|^Other Plant Sciences$'
             '|^Systems Biology$'
            )
        ],
        [ 7, #"07 agricultural and veterinary science",
            re.compile(
             '^Agribusiness$'
             '|^Agriculture$'
             '|^Agricultural Economics$'
             '|^Agricultural Education$'
             '|^Apiculture$'
             '|^Biosecurity$'
             '|^Agriculture: Viticulture and Oenology$'
             '|^Animal Sciences$'
             '|^Aquaculture and Fisheries$'
             '|^Beef Science$'
             '|^Dairy Science$'
             '|^Meat Science$'
             '|^Ornithology$'
             '|^Poultry or Avian Science$'
             '|^Sheep and Goat Science$'
             '|^Zoology$'
             '|^Other Animal Sciences$'
             '|^Forest Sciences$'
             '|^Forest Biology$'
             '|^Sciences: Forest Management$'
             '|^Sciences: Wood Science and Pulp, Paper Technology$'
             '|^Other Forestry and Forest Sciences$'
             '|^Animal Experimentation and Research$'
             '|^Fruit Science$'
             '|^Horticulture$'
             '|^Agronomy and Crop Sciences$'
             '|^Agricultural Science$'
Veterinary Medicine
Veterinary Medicine: Comparative and Laboratory Animal Medicine
Veterinary Medicine: Large or Food Animal and Equine Medicine
Veterinary Medicine: Small or Companion Animal Medicine
Veterinary Medicine: Veterinary Anatomy
Veterinary Medicine: Veterinary Infectious Diseases
Veterinary Medicine: Veterinary Microbiology and Immunobiology
Veterinary Medicine: Veterinary Pathology and Pathobiology
Veterinary Medicine: Veterinary Physiology
Veterinary Medicine: Veterinary Preventive Medicine, Epidemiology, and Public Health
Veterinary Medicine: Veterinary Toxicology and Pharmacology
Veterinary Medicine: Other Veterinary Medicine
Agricultural and Resource Economics
Food Security
            )
        ],
        [ 8, #"08 information and computing sciences",
            re.compile(
             '^Computer Engineering $'
             '|^Computer and Systems Architecture $'
             '|^Data Storage Systems $'
             '|^Digital Circuits $'
             '|^Digital Communications and Networking $'
             '|^Hardware Systems $'
             '|^Robotics $'
             '|^Other Computer Engineering $'

Computer Sciences
Artificial Intelligence and Robotics
Information Security
Databases and Information Systems
Graphics and Human Computer Interfaces
Numerical Analysis and Scientific Computing
OS and Networks
Programming Languages and Compilers
Software Engineering
Systems Architecture
Theory and Algorithms
Other Computer Sciences
Library and Information Science
Archival Science
Cataloging and Metadata
Collection Development and Management
Health Sciences and Medical Librarianship
Information Literacy
Law Librarianship
Scholarly Communication
Scholarly Publishing
            )
        ],
        [ 9, #"09 engineering",
            re.compile(
             '^Engineering$'
             '|^Aerospace Engineering$'
             '|^Aerodynamics and Fluid Mechanics$'
             '|^Aeronautical Vehicles$'
             '|^Astrodynamics$'
             '|^Multi-Vehicle Systems and Air Traffic Control$'
             '|^Navigation, Guidance, Control and Dynamics$'
             '|^Propulsion and Power$'
             '|^Space Habitation and Life Support$'
             '|^Space Vehicles$'
             '|^Structures and Materials$'
             '|^Systems Engineering and Multidisciplinary Design Optimization$'
             '|^Other Aerospace Engineering$'
             '|^Automotive Engineering$'
             '|^Military Vehicles$'
             '|^Navigation, Guidance, Control, and Dynamics$'
             '|^Aviation$'
             '|^Aviation and Space Education$'
             '|^Aviation Safety and Security$'
             '|^Maintenance Technology$'
             '|^Management and Operations$'
             '|^Chemical Engineering$'
             '|^Catalysis and Reaction Engineering$'
             '|^Complex Fluids$'
             '|^Membrane Science$'
             '|^Petroleum Engineering$'
             '|^Polymer Science$'
             '|^Process Control and Systems$'
             '|^Thermodynamics$'
             '|^Transport Phenomena$'
             '|^Other Chemical Engineering$'
             '|^Civil and Environmental Engineering$'
             '|^Civil Engineering$'
             '|^Construction Engineering and Management$'
             '|^Environmental Engineering$'
             '|^Geotechnical Engineering$'
             '|^Hydraulic Engineering$'
             '|^Structural Engineering$'
             '|^Transportation Engineering$'
             '|^Other Civil and Environmental Engineering$'
             '|^Computational Engineering$'
             '|^Engineering Education$'
             '|^Engineering Science and Materials$'
             '|^Dynamics and Dynamical Systems$'
             '|^Engineering Mechanics$'
             '|^Mechanics of Materials$'
             '|^Other Engineering Science and Materials$'
             '|^Geological Engineering $'
             '|^Materials Science and Engineering$'
             '|^Biology and Biomimetic Materials$'
             '|^Ceramic Materials$'
             '|^Metallurgy$'
             '|^Polymer and Organic Materials$'
             '|^Semiconductor and Optical Materials$'
             '|^Structural Materials$'
             '|^Other Materials Science and Engineering$'
             '|^Mechanical Engineering$'
             '|^Acoustics, Dynamics, and Controls$'
             '|^Applied Mechanics$'
             '|^Biomechanical Engineering$'
             '|^Computer-Aided Engineering and Design$'
             '|^Electro-Mechanical Systems$'
             '|^Energy Systems$'
             '|^Heat Transfer, Combustion$'
             '|^Manufacturing$'
             '|^Ocean Engineering$'
             '|^Tribology$'
             '|^Other Mechanical Engineering$'
             '|^Mining Engineering$'
             '|^Explosives Engineering$'
             '|^Nuclear Engineering$'
             '|^Operations Research, Systems Engineering and Industrial Engineering$'
             '|^Ergonomics$'
             '|^Industrial$'
             '|^Engineering$'
             '|^Industrial Technology$'
             '|^Operational Research$'
             '|^Systems Engineering$'
             '|^Other Operations$'
             '|^Research, Systems Engineering and Industrial Engineering$'
            )
        ],
        [ 10, #"10 technology",
            re.compile(
             '^Biomedical Engineering and Bioengineering $'
             '|^Bioelectrical and Neuroengineering $'
             '|^Bioimaging and Biomedical Optics $'
             '|^Biological Engineering $'
             '|^Biomaterials $'
             '|^Biomechanics and Biotransport $'
             '|^Biomedical Devices and Instrumentation $'
             '|^Molecular, Cellular, and Tissue Engineering $'
             '|^Systems and Integrative Engineering $'
             '|^Vision Science $'
             '|^Other Biomedical Engineering and Bioengineering $'
             '|^Bioresource and Agricultural Engineering $'
             '|^Biochemical and Biomolecular Engineering $'
             '|^Electrical and Computer Engineering $'
             '|^Biomedical $'
             '|^Controls and Control Theory $'
             '|^Electrical and Electronics $'
             '|^Electromagnetics and Photonics $'
             '|^Electronic Devices and Semiconductor Manufacturing $'
             '|^Nanotechnology Fabrication $'
             '|^Power and Energy $'
             '|^Signal Processing $'
             '|^Systems and Communications $'
             '|^VLSI and Circuits, Embedded and Hardware Systems $'
             '|^Other Electrical and Computer Engineering $'
             '|^Nanoscience and Nanotechnology $'
             '|^Biotechnology$'
Nanotechnology

            )
        ],
        [ 11, #"11 medical and health sciences",
            re.compile(
              '^Kinesiology$'
              '|^Biomechanics$'
              '|^Exercise Science$'
              '|^Expeditionary Education$'
              '|^Motor Control$'
              '|^Psychology of Movement$'
              '|^Other Kinesiology$'
              '|^Immunology and Infectious Disease$'
              '|^Immunity$'
              '|^Immunology of Infectious Disease$'
              '|^Immunopathology$'
              '|^Immunoprophylaxis and Therapy$'
              '|^Parasitology$'
              '|^Other Immunology and Infectious Disease$'
              '|^Nutrition$'
              '|^Comparative Nutrition$'
              '|^Human and Clinical Nutrition$'
              '|^International and Community Nutrition$'
              '|^Molecular, Genetic, and Biochemical Nutrition$'
              '|^Nutritional Epidemiology$'
              '|^Other Nutrition$'
              '|^Pharmacology, Toxicology and Environmental Health$'
              '|^Environmental Health$'
              '|^Medicinal Chemistry and Pharmaceutics$'
              '|^Pharmacology$'
              '|^Toxicology$'
              '|^Other Pharmacology, Toxicology and Environmental Health$'
              '|^Medicine and Health Sciences$'
              '|^Alternative and Complementary Medicine$'
              '|^Analytical, Diagnostic and Therapeutic Techniques and Equipment$'
              '|^Anesthesia and Analgesia$'
              '|^Diagnosis$'
              '|^Equipment and Supplies$'
              '|^Investigative Techniques$'
              '|^Surgical Procedures, Operative$'
              '|^Therapeutics$'
              '|^Other Analytical, Diagnostic and Therapeutic Techniques and Equipment$'
              '|^Anatomy$'
              '|^Animal Structures$'
              '|^Body Regions$'
              '|^Cardiovascular System$'
              '|^Cells$'
              '|^Digestive System$'
              '|^Embryonic Structures$'
              '|^Endocrine System$'
              '|^Fluids and Secretions$'
              '|^Hemic and Immune Systems$'
              '|^Integumentary System$'
              '|^Musculoskeletal System$'
              '|^Nervous System$'
              '|^Respiratory System$'
              '|^Sense Organs$'
              '|^Stomatognathic System$'
              '|^Tissues$'
              '|^Urogenital System$'
              '|^Chemicals and Drugs$'
              '|^Amino Acids, Peptides, and Proteins$'
              '|^Biological Factors$'
              '|^Biomedical and Dental Materials$'
              '|^Carbohydrates$'
              '|^Chemical Actions and Uses$'
              '|^Complex Mixtures$'
              '|^Enzymes and Coenzymes$'
              '|^Heterocyclic Compounds$'
              '|^Hormones, Hormone Substitutes, and Hormone Antagonists$'
              '|^Inorganic Chemicals$'
              '|^Lipids$'
              '|^Macromolecular Substances$'
              '|^Nucleic Acids, Nucleotides, and Nucleosides$'
              '|^Organic Chemicals$'
              '|^Pharmaceutical Preparations$'
              '|^Polycyclic Compounds$'
              '|^Other Chemicals and Drugs$'
              '|^Dentistry$'
              '|^Dental Hygiene$'
              '|^Dental Materials$'
              '|^Dental Public Health and Education$'
              '|^Endodontics and Endodontology$'
              '|^Oral and Maxillofacial Surgery$'
              '|^Oral Biology and Oral Pathology$'
              '|^Orthodontics and Orthodontology$'
              '|^Pediatric Dentistry and Pedodontics$'
              '|^Periodontics and Periodontology$'
              '|^Prosthodontics and Prosthodontology$'
              '|^Other Dentistry$'
              '|^Dietetics and Clinical Nutrition$'
              '|^Diseases$'
              '|^Animal Diseases$'
              '|^Bacterial Infections and Mycoses$'
              '|^Cardiovascular Diseases$'
              '|^Congenital, Hereditary, and Neonatal Diseases and Abnormalities$'
              '|^Digestive System Diseases$'
              '|^Disease Modeling$'
              '|^Disorders of Environmental Origin$'
              '|^Endocrine System Diseases$'
              '|^Eye Diseases$'
              '|^Female Urogenital Diseases and Pregnancy Complications$'
              '|^Hemic and Lymphatic Diseases$'
              '|^Immune System Diseases$'
              '|^Male Urogenital Diseases$'
              '|^Musculoskeletal Diseases$'
              '|^Neoplasms$'
              '|^Nervous System Diseases$'
              '|^Nutritional and Metabolic Diseases$'
              '|^Otorhinolaryngologic Diseases$'
              '|^Parasitic Diseases$'
              '|^Pathological Conditions, Signs and Symptoms$'
              '|^Respiratory Tract Diseases$'
              '|^Skin and Connective Tissue Diseases$'
              '|^Stomatognathic Diseases$'
              '|^Virus Diseases$'
              '|^Health and Medical Administration$'
              '|^Medical Sciences$'
              '|^Biochemical Phenomena, Metabolism, and Nutrition$'
              '|^Biological Phenomena, Cell Phenomena, and Immunity$'
              '|^Chemical and Pharmacologic Phenomena$'
              '|^Circulatory and Respiratory Physiology$'
              '|^Digestive, Oral, and Skin Physiology$'
              '|^Genetic Phenomena$'
              '|^Genetic Processes$'
              '|^Genetic Structures$'
              '|^Medical Anatomy$'
              '|^Medical Biochemistry$'
              '|^Medical Biomathematics and Biometrics$'
              '|^Medical Biophysics$'
              '|^Medical Biotechnology$'
              '|^Medical Cell Biology$'
              '|^Medical Genetics$'
              '|^Medical Immunology$'
              '|^Medical Microbiology$'
              '|^Medical Molecular Biology$'
              '|^Medical Neurobiology$'
              '|^Medical Nutrition$'
              '|^Medical Pathology$'
              '|^Medical Pharmacology$'
              '|^Medical Physiology$'
              '|^Medical Toxicology$'
              '|^Musculoskeletal, Neural, and Ocular Physiology$'
              '|^Neurosciences$'
              '|^Physiological Processes$'
              '|^Reproductive and Urinary Physiology$'
              '|^Other Medical Sciences$'
              '|^Medical Specialties$'
              '|^Allergy and Immunology$'
              '|^Anesthesiology$'
              '|^Behavioral Medicine$'
              '|^Cardiology$'
              '|^Critical Care$'
              '|^Dermatology$'
              '|^Emergency Medicine$'
              '|^Endocrinology, Diabetes, and Metabolism$'
              '|^Family Medicine$'
              '|^Gastroenterology$'
              '|^Geriatrics$'
              '|^Hematology$'
              '|^Hepatology$'
              '|^Infectious Disease$'
              '|^Integrative Medicine$'
              '|^Internal Medicine$'
              '|^Nephrology$'
              '|^Neurology$'
              '|^Obstetrics and Gynecology$'
              '|^Oncology$'
              '|^Ophthalmology$'
              '|^Orthopedics$'
              '|^Osteopathic Medicine and Osteopathy$'
              '|^Otolaryngology$'
              '|^Palliative Care$'
              '|^Pathology$'
              '|^Pediatrics$'
              '|^Plastic Surgery$'
              '|^Podiatry$'
              '|^Preventive Medicine$'
              '|^Primary Care$'
              '|^Psychiatry$'
              '|^Pulmonology$'
              '|^Radiation Medicine$'
              '|^Radiology$'
              '|^Rheumatology$'
              '|^Sleep Medicine$'
              '|^Sports Medicine$'
              '|^Surgery$'
              '|^Trauma$'
              '|^Tropical Medicine$'
              '|^Urology$'
              '|^Other Medical Specialties$'
              '|^Mental and Social Health$'
              '|^Animal-Assisted Therapy$'
              '|^Art Therapy$'
              '|^Clinical and Medical Social Work$'
              '|^Cognitive Behavioral Therapy$'
              '|^Community Health$'
              '|^Marriage and Family Therapy and Counseling$'
              '|^Psychiatric and Mental Health$'
              '|^Psychoanalysis and Psychotherapy$'
              '|^Substance Abuse and Addiction$'
              '|^Other Mental and Social Health$'
              '|^Nursing$'
              '|^Critical Care Nursing$'
              '|^Family Practice Nursing$'
              '|^Geriatric Nursing$'
              '|^Maternal, Child Health and Neonatal Nursing$'
              '|^Nursing Administration$'
              '|^Nursing Midwifery$'
              '|^Occupational and Environmental Health Nursing$'
              '|^Pediatric Nursing$'
              '|^Perioperative, Operating Room and Surgical Nursing$'
              '|^Psychiatric and Mental Health Nursing$'
              '|^Public Health and Community Nursing$'
              '|^Other Nursing$'
              '|^Pharmacy and Pharmaceutical Sciences$'
              '|^Medicinal and Pharmaceutical Chemistry$'
              '|^Natural Products Chemistry and Pharmacognosy$'
              '|^Pharmaceutics and Drug Design$'
              '|^Pharmacoeconomics and Pharmaceutical Economics$'
              '|^Pharmacy Administration, Policy and Regulation$'
              '|^Other Pharmacy and Pharmaceutical Sciences$'
              '|^Public Health$'
              '|^Clinical Epidemiology$'
              '|^Community Health and Preventive Medicine$'
              '|^Environmental Public Health$'
              '|^Epidemiology$'
              '|^Health and Medical Physics$'
              '|^Health Services Administration$'
              '|^Health Services Research$'
              '|^Influenza Humans$'
              '|^Influenza Virus Vaccines$'
              '|^International Public Health$'
              '|^Maternal and Child Health$'
              '|^Occupational Health and Industrial Hygiene$'
              '|^Patient Safety$'
              '|^Public Health Education and Promotion$'
              '|^Women\'s Health$'
              '|^Other Public Health$'
              '|^Rehabilitation and Therapy$'
              '|^Kinesiotherapy$'
              '|^Movement and Mind-Body Therapies$'
              '|^Occupational Therapy$'
              '|^Orthotics and Prosthetics$'
              '|^Physical Therapy$'
              '|^Physiotherapy$'
              '|^Recreational Therapy$'
              '|^Respiratory Therapy$'
              '|^Somatic Bodywork and Related Therapeutic Practices$'
              '|^Vocational Rehabilitation Counseling$'
              '|^Other Rehabilitation and Therapy$'
              '|^Translational Medical Research$'
              '|^Nanomedicine$'
            )
        ],
        [ 12, #"12 built environment and design",
            re.compile(
                '^Architectural Engineering$'
                '|^Architectural History and Criticism$'
                '|^Architectural Technology$'
                '|^Construction Engineering$'
                '|^Environmental Design$'
                '|^Historic Preservation and Conservation$'
                '|^Interior Architecture$'
                '|^Landscape Architecture$'
                '|^Other Architecture$'
             )
        ],
        [ 13, #"13 education",
            re.compile(
             '^Education'
             '|^Adult and Continuing Education'
             '|^Art Education'
             '|^Bilingual, Multilingual, and Multicultural Education'
             '|^Community College Leadership'
             '|^Curriculum and Instruction'
             '|^Curriculum and Social Inquiry'
             '|^Disability and Equity in Education'
             '|^Disability and Equity in Accessibility'
             '|^Disability and Equity in Gender Equity in Education'
             '|^Early Childhood Education'
             '|^Education Economics'
             '|^Educational Administration and Supervision'
             '|^Adult and Continuing Education Administration'
             '|^Community College Education Administration'
             '|^Elementary and Middle and Secondary Education Administration'
             '|^Higher Education Administration'
             '|^Special Education Administration'
             '|^Urban Education'
             '|^Other Educational Administration and Supervision'
             '|^Educational Assessment, Evaluation, and Research'
             '|^Educational Leadership'
             '|^Educational Methods'
             '|^Educational Psychology'
             '|^Educational Technology'
             '|^Elementary Education'
             '|^Gifted Education'
             '|^Health and Physical Education'
             '|^Higher Education'
             '|^Higher Scholarship of Teaching and Learning'
             '|^Higher University Extension'
             '|^Home Economics'
             '|^Humane Education'
             '|^Indigenous Education'
             '|^Instructional Media Design'
             '|^International and Comparative Education'
             '|^Language and Literacy Education'
             '|^Liberal Studies'
             '|^Online and Distance Education'
             '|^Outdoor Education'
             '|^Prison Education and Reentry'
             '|^Science and Mathematics Education'
             '|^Secondary Education'
             '|^Social and Philosophical Foundations of Education'
             '|^Special Education and Teaching'
             '|^Student Counseling and Personnel Services'
             '|^Student Counseling and Personnel Services: Academic Advising'
             '|^Teacher Education and Professional Development'
             '|^Adult and Continuing Education and Teaching'
             '|^Elementary Education and Teaching'
             '|^Higher Education and Teaching'
             '|^Junior High, Intermediate, Middle School Education and Teaching'
             '|^Pre-Elementary, Early Childhood, Kindergarten Teacher Education'
             '|^Secondary Education and Teaching'
             '|^Other Teacher Education and Professional Development'
             '|^Other Education'
             '|^Vocational Education'
            )
        ],
        [ 14, #"14 economics",
            re.compile(
Economics
Behavioral Economics
Econometrics
Economic History
Economic Theory
Finance
Growth and Development
Health Economics
Income Distribution
Industrial Organization
International Economics
Labor Economics
Macroeconomics
Political Economy
Public Economics
Regional Economics
Other Economics
            )
        ],
        [ 15, #"15 commerce, management, tourism and services",
            re.compile(
             '^Business$'
             '|^Accounting$'
             '|^Advertising and Promotion Management$'
             '|^Arts Management$'
             '|^Arts Management: Music Business$'
             '|^Business Administration, Management, and Operations$'
             '|^Business Analytics$'
             '|^Business and Corporate Communications$'
             '|^Business Intelligence$'
             '|^E-Commerce$'
             '|^Entrepreneurial and Small Business Operations$'
             '|^Fashion Business$'
             '|^Finance and Financial Management$'
             '|^Hospitality Administration and Management$'
             '|^Hospitality Administration and Management: Food and Beverage Management$'
             '|^Hospitality Administration and Management: Gaming and Casino Operations Management$'
             '|^Human Resources Management$'
             '|^Human Resources Management: Benefits and Compensation $'
             '|^Human Resources Management: Performance Management$'
             '|^Human Resources Management: Training and Development$'
             '|^International Business$'
             '|^Labor Relations$'
             '|^Labor Relations: Collective Bargaining$'
             '|^Labor Relations: International and Comparative Labor Relations$'
             '|^Labor Relations: Unions$'
             '|^Management Information Systems$'
             '|^Marketing$'
             '|^Management Sciences and Quantitative Methods$'
             '|^Nonprofit Administration and Management$'
             '|^Operations and Supply Chain Management$'
             '|^Organizational Behavior and Theory$'
             '|^Portfolio and Security Analysis$'
             '|^Real Estate$'
             '|^Recreation Business$'
             '|^Sales and Merchandising$'
             '|^Sports Management$'
             '|^Strategic Management Policy$'
             '|^Technology and Innovation$'
             '|^Tourism and Travel$'
            )
        ],
        [ 16, #"16 studies in human society",
            re.compile(
             '^Feminist, Gender, and Sexuality Studies$'
             '|^Lesbian, Gay, Bisexual, and Transgender Studies$'
             '|^Women\'s Studies$'
             '|^Other Feminist, Gender, and Sexuality Studies$'
             '|^Race, Ethnicity and Post-Colonial Studies$'
             '|^African American Studies$'
             '|^Asian American Studies$'
             '|^Chicana/o Studies$'
             '|^Ethnic Studies$'
             '|^Indigenous Studies$'
             '|^Latina/o Studies$'
             '|^Linguistic Anthropology$'
             '|^Anthropology$'
             '|^Folklore$'
             '|^Social and Cultural Anthropology$'
             '|^International and Area Studies$'
             '|^IAfrican Studies$'
             '|^IAsian Studies$'
             '|^IEastern European Studies$'
             '|^ILatin American Studies$'
             '|^INear and Middle Eastern Studies$'
             '|^ISoviet and Post-Soviet Studies$'
             '|^IOther International and Area Studies$'
             '|^Political Science$'
             '|^American Politics$'
             '|^Comparative Politics$'
             '|^International Relations$'
             '|^Models and Methods$'
             '|^Political Theory$'
             '|^Other Political Science$'
             '|^Family, Life Course, and Society$'
             '|^Gender and Sexuality$'
             '|^Gerontology$'
             '|^Human Ecology$'
             '|^Inequality and Stratification$'
             '|^Medicine and Health$'
             '|^Migration Studies$'
             '|^Place and Environment$'
             '|^Politics and Social Change$'
             '|^Quantitative, Qualitative, Comparative, and Historical Methodologies$'
             '|^Race and Ethnicity$'
             '|^Regional Sociology$'
             '|^Rural Sociology$'
             '|^Service Learning$'
             '|^Social Control, Law, Crime, and Deviance$'
             '|^Social Psychology and Interaction$'
             '|^Sociology of Culture$'
             '|^Sociology of Religion$'
             '|^Theory, Knowledge and Science$'
             '|^Tourism$'
             '|^Work, Economy and Organizations$'
             '|^Other Sociology$'
             '|^Public Affairs, Public Policy and Public Administration$'
             '|^Defense and Security Studies$'
             '|^Economic Policy$'
             '|^Education Policy$'
             '|^Emergency and Disaster Management$'
             '|^Energy Policy$'
             '|^Environmental Policy$'
             '|^Fire Science and Firefighting$'
             '|^Health Policy$'
             '|^Infrastructure$'
             '|^Military and Veterans Studies$'
             '|^Peace and Conflict Studies$'
             '|^Policy Design, Analysis, and Evaluation$'
             '|^Policy History, Theory, and Methods$'
             '|^Public Administration$'
             '|^Public Affairs$'
             '|^Public Policy$'
             '|^Recreation, Parks and Tourism Administration$'
             '|^Science and Technology Policy$'
             '|^Social Policy$'
             '|^Social Welfare$'
             '|^Terrorism Studies$'
             '|^Transportation$'
             '|^Urban Studies$'
             '|^Other Public Affairs, Public Policy and Public Administration$'
             '|^Social Work$'
             '|^Sociology$'
             '|^Civic and Community Engagement$'
             '|^Community-Based Learning$'
             '|^Community-Based Research$'
             '|^Criminology$'
             '|^Demography, Population, and Ecology$'
             '|^Domestic and Intimate Partner Violence$'
             '|^Educational Sociology$'
            )
        ],
        [ 17, #"17 psychology and cognitive sciences",
            re.compile(
             '^Psychology$'
             '|^Applied Behavior Analysis$'
             '|^Biological Psychology$'
             '|^Child Psychology$'
             '|^Clinical Psychology$'
             '|^Cognition and Perception$'
             '|^Cognitive Psychology$'
             '|^Community Psychology$'
             '|^Comparative Psychology$'
             '|^Counseling Psychology$'
             '|^Developmental Psychology$'
             '|^Experimental Analysis of Behavior$'
             '|^Geropsychology$'
             '|^Health Psychology$'
             '|^Human Factors Psychology$'
             '|^Industrial and Organizational Psychology$'
             '|^Multicultural Psychology$'
             '|^Pain Management$'
             '|^Personality and Social Contexts$'
             '|^Quantitative Psychology$'
             '|^School Psychology$'
             '|^Social Psychology$'
             '|^Theory and Philosophy$'
             '|^Transpersonal Psychology$'
             '|^Other Psychology$'
            )
        ],
        [ 18, #"18 law and legal studies",
            re.compile(
             '^Law$'
             '|^Accounting Law$'
             '|^Administrative Law$'
             '|^Admiralty$'
             '|^Agency$'
             '|^Agriculture Law$'
             '|^Air and Space Law$'
             '|^Animal Law$'
             '|^Antitrust and Trade Regulation$'
             '|^Banking and Finance Law$'
             '|^Bankruptcy Law$'
             '|^Business Organizations Law$'
             '|^Civil Law$'
             '|^Civil Procedure$'
             '|^Civil Rights and Discrimination$'
             '|^Commercial Law$'
             '|^Common Law$'
             '|^Communications Law$'
             '|^Comparative and Foreign Law$'
             '|^Computer Law$'
             '|^Conflict of Laws$'
             '|^Constitutional Law$'
             '|^Construction Law$'
             '|^Consumer Protection Law$'
             '|^Contracts$'
             '|^Courts$'
             '|^Criminal Law$'
             '|^Criminal Procedure$'
             '|^Cultural Heritage Law$'
             '|^Disability Law$'
             '|^Disaster Law$'
             '|^Dispute Resolution and Arbitration$'
             '|^Education Law$'
             '|^Elder Law$'
             '|^Election Law$'
             '|^Energy and Utilities Law$'
             '|^Entertainment, Arts, and Sports Law$'
             '|^Environmental Law$'
             '|^Estates and Trusts$'
             '|^European Law$'
             '|^Evidence$'
             '|^Family Law$'
             '|^First Amendment$'
             '|^Food and Drug Law$'
             '|^Fourteenth Amendment$'
             '|^Fourth Amendment$'
             '|^Gaming Law$'
             '|^Government Contracts$'
             '|^Health Law and Policy$'
             '|^Housing Law$'
             '|^Human Rights Law$'
             '|^Immigration Law$'
             '|^Indian and Aboriginal Law$'
             '|^Insurance Law$'
             '|^Intellectual Property Law$'
             '|^International Humanitarian Law$'
             '|^International Law$'
             '|^International Trade Law$'
             '|^Internet Law$'
             '|^Judges$'
             '|^Jurisdiction$'
             '|^Jurisprudence$'
             '|^Juvenile Law$'
             '|^Labor and Employment Law$'
             '|^Land Use Law$'
             '|^Law and Economics$'
             '|^Law and Gender$'
             '|^Law and Philosophy$'
             '|^Law and Politics$'
             '|^Law and Psychology$'
             '|^Law and Race$'
             '|^Law and Society$'
             '|^Law Enforcement and Corrections$'
             '|^Law of the Sea$'
             '|^Legal Biography$'
             '|^Legal Education$'
             '|^Legal Ethics and Professional Responsibility$'
             '|^Legal History$'
             '|^Legal Profession$'
             '|^Legal Remedies$'
             '|^Legal Writing and Research$'
             '|^Legislation$'
             '|^Litigation$'
             '|^Marketing Law$'
             '|^Medical Jurisprudence$'
             '|^Military, War, and Peace$'
             '|^National Security Law$'
             '|^Natural Law$'
             '|^Natural Resources Law$'
             '|^Nonprofit Organizations Law$'
             '|^Oil, Gas, and Mineral Law$'
             '|^Organizations Law$'
             '|^President/Executive Department$'
             '|^Privacy Law$'
             '|^Property Law and Real Estate$'
             '|^Public Law and Legal Theory$'
             '|^Religion Law$'
             '|^Retirement Security Law$'
             '|^Rule of Law$'
             '|^Science and Technology Law$'
             '|^Second Amendment$'
             '|^Secured Transactions$'
             '|^Securities Law$'
             '|^Sexuality and the Law$'
             '|^Social Welfare Law$'
             '|^State and Local Government Law$'
             '|^Supreme Court of the United States$'
             '|^Tax Law$'
             '|^Taxation-Federal$'
             '|^Taxation-Federal Estate and Gift$'
             '|^Taxation-State and Local$'
             '|^Taxation-Transnational$'
             '|^Torts$'
             '|^Transnational Law$'
             '|^Transportation Law$'
             '|^Water Law$'
             '|^Workers\' Compensation Law$'
             '|^Other Law$'
             '|^Legal Studies$'
             '|^Studies: Criminology and Criminal Justice$'
             '|^Forensic Science and Technology$'
             '|^Legal Theory$'
             '|^Other Legal Studies$'
            )
        ],
        [ 19, #"19 studies in creative arts and writing",
            re.compile(
                 '^American Film Studies$'
                 '|^Art and Design$'
                 '|^Art and Materials Conservation$'
                 '|^Book and Paper$'
                 '|^Ceramic Arts$'
                 '|^Fashion Design$'
                 '|^Fiber, Textile, and Weaving Arts$'
                 '|^Furniture Design$'
                 '|^Game Design$'
                 '|^Glass Arts$'
                 '|^Graphic Design$'
                 '|^Illustration$'
                 '|^Industrial and Product Design$'
                 '|^Interactive Arts$'
                 '|^Interdisciplinary Arts and Media$'
                 '|^Interior Design$'
                 '|^Metal and Jewelry Arts$'
                 '|^Painting$'
                 '|^Printmaking$'
                 '|^Sculpture$'
                 '|^Art Practice$'
                 '|^Audio Arts and Acoustics$'
                 '|^Creative Writing$'
                 '|^Fiction$'
                 '|^Nonfiction$'
                 '|^Poetry$'
                 '|^Film and Media Studies$'
                 '|^Film Production$'
                 '|^Screenwriting$'
                 '|^Visual Studies$'
                 '|^Other Film and Media Studies$'
                 '|^Fine Arts$'
                 '|^Music$'
                 '|^Composition$'
                 '|^Ethnomusicology$'
                 '|^Music Education$'
                 '|^Music Practice$'
                 '|^Music Theory$'
                 '|^Musicology$'
                 '|^Music Pedagogy$'
                 '|^Music Performance$'
                 '|^Music Therapy$'
                 '|^Other Music$'
                 '|^Photography$'
                 '|^Radio$'
                 '|^Television$'
                 '|^Theatre and Performance Studies$'
                 '|^Acting$'
                 '|^Dance$'
                 '|^Dramatic Literature, Criticism and Theory$'
                 '|^Performance Studies$'
                 '|^Playwriting$'
                 '|^Theatre History$'
                 '|^Other Theatre and Performance Studies$'
            )
        ],
        [ 20, #"20 language, communication and culture",
            re.compile(
                 '^African Languages and Societies$'
                 '|^Africana Studies$'
                 '|^American Studies$'
                 '|^American Literature$'
                 '|^American Material Culture$'
                 '|^American Popular Culture$'
                 '|^Appalachian Studies$'
                 '|^Australian Studies$'
                 '|^Basque Studies$'
                 '|^Celtic Studies$'
                 '|^Classics$'
                 '|^Byzantine and Modern Greek$'
                 '|^Classical Literature and Philology$'
                 '|^Indo-European Linguistics and Philology$'
                 '|^Comparative Literature$'
                 '|^Translation Studies$'
                 '|^Dutch Studies$'
                 '|^East Asian Languages and Societies$'
                 '|^Chinese Studies$'
                 '|^Japanese Studies$'
                 '|^Korean Studies$'
                 '|^English Language and Literature$'
                 '|^Children\'s and Young Adult Literature$'
                 '|^Literature in English, Anglophone outside British Isles and North America$'
                 '|^Literature in English, British Isles$'
                 '|^Literature in English, North America$'
                 '|^Literature in English, North America, Ethnic and Cultural Minority$'
                 '|^Other English Language and Literature$'
                 '|^European Languages and Societies$'
                 '|^French and Francophone Language and Literature$'
                 '|^French and Francophone Literature$'
                 '|^French Linguistics$'
                 '|^Other French and Francophone Language and Literature$'
                 '|^German Language and Literature$'
                 '|^German Linguistics$'
                 '|^German Literature$'
                 '|^Other German Language and Literature$'
                 '|^Italian Language and Literature$'
                 '|^Italian Linguistics$'
                 '|^Italian Literature$'
                 '|^Other Italian Language and Literature$'
                 '|^Jewish Studies$'
                 '|^Yiddish Language and Literature$'
                 '|^Language Interpretation and Translation$'
                 '|^Latin American Languages and Societies$'
                 '|^Caribbean Languages and Societies$'
                 '|^Modern Languages$'
                 '|^Modern Literature$'
                 '|^Near Eastern Languages and Societies$'
                 '|^Pacific Islands Languages and Societies$'
                 '|^Hawaiian Studies$'
                 '|^Melanesian Studies$'
                 '|^Micronesian Studies$'
                 '|^Polynesian Studies$'
                 '|^Reading and Language$'
                 '|^Scandinavian Studies$'
                 '|^Sign Languages$'
                 '|^American Sign Language$'
                 '|^Slavic Languages and Societies$'
                 '|^Russian Linguistics$'
                 '|^Russian Literature$'
                 '|^South and Southeast Asian Languages and Societies$'
                 '|^Spanish and Portuguese Language and Literature$'
                 '|^Latin American Literature$'
                 '|^Portuguese Literature$'
                 '|^Spanish Linguistics$'
                 '|^Spanish Literature$'
                 '|^Other Spanish and Portuguese Language and Literature$'
                 '|^Linguistics$'
                 '|^Anthropological Linguistics and Sociolinguistics$'
                 '|^Applied Linguistics$'
                 '|^Comparative and Historical Linguistics$'
                 '|^Computational Linguistics$'
                 '|^Discourse and Text Linguistics$'
                 '|^First and Second Language Acquisition$'
                 '|^Language Description and Documentation$'
                 '|^Morphology$'
                 '|^Phonetics and Phonology$'
                 '|^Psycholinguistics and Neurolinguistics$'
                 '|^Semantics and Pragmatics$'
                 '|^Syntax$'
                 '|^Typological Linguistics and Linguistic Diversity$'
                 '|^Other Linguistics$'
            )
        ],
        [ 21, #"21 history and archaeology",
            re.compile(
                 '^Ancient History, Greek and Roman through Late Antiquity$'
                 '|^Classical Archaeology and Art History$'
                 '|^History$'
                 '|^African History$'
                 '|^Asian History$'
                 '|^Canadian History$'
                 '|^Cultural History$'
                 '|^Diplomatic History$'
                 '|^European History$'
                 '|^Genealogy$'
                 '|^History of Gender$'
                 '|^History of the Pacific Islands$'
                 '|^History of Religion$'
                 '|^History of Science, Technology, and Medicine$'
                 '|^Holocaust and Genocide Studies$'
                 '|^Intellectual History$'
                 '|^Islamic World and Near East History$'
                 '|^Labor History$'
                 '|^Latin American History$'
                 '|^Legal$'
                 '|^Medieval History$'
                 '|^Military History$'
                 '|^Oral History$'
                 '|^Political History$'
                 '|^Public History$'
                 '|^Social History$'
                 '|^United States History$'
                 '|^Women\'s History$'
                 '|^Other History$'
                 '|^Medieval Studies$'

            )
        ],
        [ 22, #"22 philosophy and religious studies",
            re.compile(
                 '^Ancient Philosophy$'
                 '|^Philosophy$'
                 '|^Applied Ethics$'
                 '|^Comparative Philosophy$'
                 '|^Continental Philosophy$'
                 '|^Epistemology$'
                 '|^Esthetics$'
                 '|^Ethics and Political Philosophy$'
                 '|^Feminist Philosophy$'
                 '|^History of Philosophy$'
                 '|^Logic and Foundations of Mathematics$'
                 '|^Metaphysics$'
                 '|^Philosophy of Language$'
                 '|^Philosophy of Mind$'
                 '|^Philosophy of Science$'
                 '|^Other Philosophy$'
                 '|^Religion$'
                 '|^Biblical Studies$'
                 '|^Buddhist Studies$'
                 '|^Catholic Studies$'
                 '|^Christianity$'
                 '|^Christian Denominations and Sects$'
                 '|^Comparative Methodologies and Theories$'
                 '|^Ethics in Religion$'
                 '|^Hindu Studies$'
                 '|^History of Christianity$'
                 '|^History of Religions of Eastern Origins$'
                 '|^History of Religions of Western Origin$'
                 '|^Islamic Studies$'
                 '|^Liturgy and Worship$'
                 '|^Missions and World Christianity$'
                 '|^Mormon Studies$'
                 '|^New Religious Movements$'
                 '|^Practical Theology$'
                 '|^Religious Education$'
                 '|^Religious Thought, Theology and Philosophy of Religion$'
                 '|^Other Religion$'
                 '|^Bioethics and Medical Ethics$'
            )
        ]
]