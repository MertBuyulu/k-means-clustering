# import statements
import numpy as np
import pandas as pd
import requests
import re
import string

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
        stripped = [re.sub(regex, '', input).lower() for input in self.raw_input]
        return [(input.translate(str.maketrans('', '', string.punctuation))).rstrip() for input in stripped]

    def jaccard(self, tweet1, tweet2):
        set1 = set(tweet1.split())
        set2 = set(tweet2.split())
        return (len(set1.union(set2)) - len(set1.intersection(set2))) / len(set1.union(set2))

    # Fit function
    def cluster_data(self, k=3, iterations=50):
        centroid_indices = np.random.choice(len(self.procesed_input), k, replace=False)
        centroids = []
        for i in centroid_indices:
            centroids.append(self.procesed_input[i])

        for iter in iterations:

            pass


    def converged(self):
        pass

    def cluster_assignment(self):
        cluster_dict = dict()
        for tweet in self.procesed_input:
            pass

        pass

if __name__ == "__main__":
    dataUrl = 'https://raw.githubusercontent.com/MertBuyulu/k-means-clustering/main/nytimeshealth.txt'
    k_means = KMeans(dataUrl)
    #print(k_means.procesed_input)
