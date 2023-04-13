# import statements
import numpy as np
import pandas as pd

class KMeans():
    def __init__(self, dataFile):
        self.raw_data = pd.read_csv(dataFile, header=None)
        print(self.raw_data)

    # TODO: preprocess the data file
    def preprocess_data(self):
        pass
    
    #
    def cluster_data(self):
        pass 

if __name__ == "__main__":
    # k_means = KMeans("")
    pass
