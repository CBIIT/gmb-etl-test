import logging
import os
import sys
from tkinter import E
import yaml
import argparse
import shutil
import xml.etree.ElementTree
from rave_extraction.gmb_rave_extractor import RaveExtractor

parser = argparse.ArgumentParser()
parser.add_argument('config_file', help='The name of the config file')
args = parser.parse_args()
config_file = args.config_file

# Load the configuration file
with open(config_file) as f:
    config = yaml.load(f, Loader = yaml.FullLoader)

try:
    # Extract the Rave Data
    rave_extractor = RaveExtractor(config)
    rave_data_parsed=rave_extractor.extract_rave_data()
    subject_counts = rave_extractor.count_rave_patients(rave_data_parsed)
    print(subject_counts)
except Exception as e:
    logging.error(e)
    sys.exit(1)
