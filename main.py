# import statements
import numpy as np
import requests
import re
import string
import random
import math

class KMeans():
    # default constructor
    def __init__(self, dataUrl):
        self.raw_input = self._get_data(dataUrl)
        self.procesed_input = self._preprocess_data()

    # retrieves the dataset from the specified URL
    def _get_data(self, dataUrl):
        response = requests.get(dataUrl)
        # check whether the response is good
        if response.status_code == 200:
            # get each line from the file on the new line character
            return response.text.split('\n')

    # preprocesses the data by removing special characters, punctuation, and converts the tweet to lower case
    def _preprocess_data(self):
        regex = "^\d+\|.*?\||@\w+\s?|#|http\S+"
        stripped = [re.sub(regex, '', input).lower() for input in self.raw_input]
        return [(input.translate(str.maketrans('', '', string.punctuation))).rstrip() for input in stripped]

    # Jaccard distance metric
    def jaccard(self, tweet1, tweet2):
        set1 = set(tweet1.split())
        set2 = set(tweet2.split())
        return (len(set1.union(set2)) - len(set1.intersection(set2))) / len(set1.union(set2))

    # fit function
    def cluster_data(self, k=8, iterations=300):
        # randomly select centroids
        centroid_indices = np.random.choice(len(self.procesed_input), k, replace=False)
        centroids = []
        prev_centroids = []
        clusters = dict()

        # assign centroids
        for i in centroid_indices:
            centroids.append(self.procesed_input[i])

        for iter in range(iterations):
            # check if converged for early stop
            if self.converged(centroids, prev_centroids): break

            # clusters is a dictionary that will hold the centroid as the key and a list of the tweets in the cluster as the value
            # assign tweets to the nearest centroid
            clusters = self.cluster_assignment(centroids)

            # save previous centroids for convergence check
            prev_centroids = centroids

            # assign new centroids
            centroids = self.centroid_update(clusters, prev_centroids)

        # print evaluation metrics
        self.evaluation_metrics(k, clusters)

    # cluster assignment step
    def cluster_assignment(self, centroids):
        # clusters is a dictionary of lists, with the centroid as the key and the list containing the tweets assigned to that centroid
        clusters = {new_list: [] for new_list in centroids}

        # find the closest centroid to each tweet
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
            
            # assign nearest centroid
            clusters[minimum_centroid].append(tweet)
            
        return clusters

    # updates centroids after assignment
    def centroid_update(self, clusters, prev_centroids):
        new_centroids = []

        for centroid in prev_centroids:
            # create an n x n distance matrix for calculating the new centroid of the cluster
            distance_matrix = [[-1 for _ in range(len(clusters[centroid]))] for _ in range(len(clusters[centroid]))]

            # calculate the distance between every two tweets in the cluster
            for index1, tweet1 in enumerate(clusters[centroid]):
                for index2, tweet2 in enumerate(clusters[centroid]):
                    # only calculate the distance if it hasn't already been calculated
                    if distance_matrix[index1][index2] == -1:
                        distance = self.jaccard(tweet1, tweet2)
                        distance_matrix[index1][index2] = distance
                        distance_matrix[index2][index1] = distance

            # use the row sums to find the tweet that is closest to all other tweets in the cluster
            row_sum = list(map(sum, distance_matrix))
            minimum_distance = min(row_sum)
            
            # select minimum distance tweet as the new centroid
            new_centroids.append(clusters[centroid][row_sum.index(minimum_distance)])

        return new_centroids

    # convergence check
    # returns true if the current and previous iteration centroids are the same
    def converged(self, centroids, prev_centroids):
        return (set(centroids) == set(prev_centroids))
    
    # calculates the sum squared error for the single run
    def sse(self, clusters):
        sse = 0
        for centroid in clusters:
            for tweet in clusters[centroid]:
                sse += (self.jaccard(tweet, centroid) ** 2)

        return sse
    
    # prints evaluation metrics including k, SSE, and number of tweets per cluster
    def evaluation_metrics(self, k, clusters):
        print('K =', k)
        print('SSE =', self.sse(clusters))
        cluster_num = 1
        for centroid in clusters:
            print(cluster_num, '-', len(clusters[centroid]), 'tweets')
            cluster_num += 1

# main function
if __name__ == "__main__":
    dataUrl = 'https://raw.githubusercontent.com/MertBuyulu/k-means-clustering/main/nytimeshealth.txt'
    k_means = KMeans(dataUrl)

    # runs the algorithm on 5 different values of k with iterations=300
    for k in [4, 6, 8, 10, 12]:
        k_means.cluster_data(k, iterations=300)
        print()