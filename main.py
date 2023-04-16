# import statements
import numpy as np
import pandas as pd
import requests
import re

class KMeans():
    def __init__(self, dataUrl):
        self.raw_input = self._get_data(dataUrl)
        self.procesed_input = self._preprocess_data()

    def _get_data(self, dataUrl):
        response = requests.get(dataUrl)
        # check whether the response is good
        if response.status_code == 200:
            # get each line from the file on the new line character
            return response.text.split('\n')

    def _preprocess_data(self):
        regex = "^\d+\|.*?\||@\w+\s?|#|http\S+"
        return [re.sub(regex, '', input).lower() for input in self.raw_input]

    # Fit function
    def cluster_data(self):
        pass 

if __name__ == "__main__":
    dataUrl = 'https://raw.githubusercontent.com/MertBuyulu/k-means-clustering/main/nytimeshealth.txt'
    k_means = KMeans(dataUrl)
