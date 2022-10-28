import json
import requests
import xml.etree.ElementTree as ET
import logging
import io
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
class RaveExtractor():
    def __init__(self, config):
        logging.info('Instantiating the Rave Extractor Class')
        logging.info(config)
        self.config = config

    # This method extracts the metadata from the Rave URL stored in
    # the config file .
    def extract_rave_data(self):
        # Hits the RAVE API and extracts the data 
        r = requests.get(self.config['RAVE_API_URL'], auth = HTTPBasicAuth(self.config['RAVE_USERNAME'], self.config['RAVE_PASSWORD'])) # Download data from RAVE
        # Decode the raw data
        rave_raw_data_utf8 = r.content.decode("utf-8")
        # Convert the data into a BS object and return it   
        rave_data_parsed = BeautifulSoup(rave_raw_data_utf8, 'html.parser')
        return rave_data_parsed

 
    # This method counts and returns number of patients.
    def count_rave_patients(self, parsed_data):
        # Retrieve the clinical data element
        # Count and return number of patients ONLY if their MetaDataVersionOID matches the config file
        result=parsed_data.find_all("clinicaldata",attrs={"metadataversionoid": self.config['VERSION_NUMBER']})
        return len(result)
        