# import statements
import numpy as np
import pandas as pd
import requests
import re
import string
import random

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
            # clusters is a dictionary that will hold the centroid as the key and a list of the tweets in the cluster
            clusters, sse = self.cluster_assignment(centroids)

            new_centroids = self.centroid_update()

            if self.converged(centroids, new_centroids): break
            pass


    # convergence check
    def converged(self, centroids, new_centroids):
        pass

    # cluster assignment step
    def cluster_assignment(self, centroids):
        clusters = {new_list: [] for new_list in centroids}
        sse = {val: 0 for val in self.procesed_input}

        for tweet in self.procesed_input:
            minimum_distance = 1
            minimum_centroid = None

            for centroid in centroids:
                distance = self.jaccard(tweet, centroid)
                if distance < minimum_distance:
                    minimum_distance = distance
                    minimum_centroid = centroid

            # random assignment of centroid if 0 similarity
            if minimum_distance == 1:
                minimum_centroid = random.choice(centroids)
            
            clusters[minimum_centroid].append(tweet)
            sse[tweet] = minimum_distance ** 2
            
        return clusters, sse

    # updates centroids after assignment
    def centroid_update(self):
        pass

if __name__ == "__main__":
    dataUrl = 'https://raw.githubusercontent.com/MertBuyulu/k-means-clustering/main/nytimeshealth.txt'
    k_means = KMeans(dataUrl)
    #print(k_means.procesed_input)
