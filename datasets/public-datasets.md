# Datasets
To accelerate personal and collaborative work with others, this doc will serve as a resource for identifying datasets that I'm personally interested in exploring for a specific purpose (e.g. disease-specific, technology-specific). One of the other priorities are to locate datasets that are well-curated, publicly accessible, and usually free. 

## images
- MIMIC-IV CXR
- MIMIC-IV CXR JPEG
- TCIA

## Electronic health records (EHR)
- MIMIC-IV
- EHRSHOT

### MIMIC-IV


### [EHRSHOT](https://github.com/som-shahlab/ehrshot-benchmark)
EHRSHOT is a benchmark dataset of structured electronic health record data (i.e., no images or clinical text) for 6712 patients. EHRShot contains a total of 39.2 million observations (diagnoses, procedures, medications, lab results, etc.) and 893,773 unique visits. All data is sourced from Stanford’s STARR-OMOP database and is fully deidentified. Unlike most EHR research datasets, EHRSHOT is not restricted to ED/ICU visits and includes longitudinal patient data for all hospital encounter types. EHRSHOT targets the few-shot evaluation of foundation models and includes 15 classification tasks (such as 30-day readmission, abnormal lab value prediction, and chest X-ray finding prediction). Please see our Github repo to obtain code for loading the dataset and running a set of pre-trained baseline models:https://github.com/som-shahlab/ehrshot-benchmark

