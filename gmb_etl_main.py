import os
import sys
import yaml
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('config_file', help='The name of the config file')
args = parser.parse_args()
config_file = args.config_file

# Load the configuration file
with open(config_file) as f:
    config = yaml.load(f, Loader = yaml.FullLoader)