# import statements
import numpy as np
import pandas as pd
import requests
import re
import string
import random
import math

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
        prev_centroids = []
        clusters = dict()
        for i in centroid_indices:
            centroids.append(self.procesed_input[i])

        for iter in range(iterations):
            if self.converged(centroids, prev_centroids): break

            # clusters is a dictionary that will hold the centroid as the key and a list of the tweets in the cluster as the value
            clusters = self.cluster_assignment(centroids)

            prev_centroids = centroids
            centroids = self.centroid_update(clusters, prev_centroids)

        self.evaluation_metrics(k, clusters)

    # cluster assignment step
    def cluster_assignment(self, centroids):
        clusters = {new_list: [] for new_list in centroids}

        for tweet in self.procesed_input:
            minimum_distance = math.inf
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
            
        return clusters

    # updates centroids after assignment
    def centroid_update(self, clusters, prev_centroids):
        new_centroids = []

        for centroid in prev_centroids:
            distance_matrix = [[-1 for _ in range(len(clusters[centroid]))] for _ in range(len(clusters[centroid]))]

            for index1, tweet1 in enumerate(clusters[centroid]):
                for index2, tweet2 in enumerate(clusters[centroid]):
                    if distance_matrix[index1][index2] == math.inf:
                        distance = self.jaccard(tweet1, tweet2)
                        distance_matrix[index1][index2] = distance
                        distance_matrix[index2][index1] = distance

            row_sum = list(map(sum, distance_matrix))
            minimum_distance = min(row_sum)
            new_centroids.append(clusters[centroid][row_sum.index(minimum_distance)])

        return new_centroids

    # convergence check
    def converged(self, centroids, new_centroids):
        return (set(centroids) == set(new_centroids))
    
    def sse(self, clusters):
        sse = 0
        for centroid in clusters:
            for tweet in clusters[centroid]:
                sse += (self.jaccard(tweet, centroid) ** 2)

        return sse
    
    def evaluation_metrics(self, k, clusters):
        print('K =', k)
        print('SSE =', self.sse(clusters))
        cluster_num = 1
        for centroid in clusters:
            print(cluster_num, '-', len(clusters[centroid]), 'tweets')
            cluster_num += 1

if __name__ == "__main__":
    dataUrl = 'https://raw.githubusercontent.com/MertBuyulu/k-means-clustering/main/nytimeshealth.txt'
    k_means = KMeans(dataUrl)

    for k in [4, 6, 8, 10, 12]:
        k_means.cluster_data(k, iterations=100)
