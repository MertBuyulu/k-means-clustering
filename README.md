# 4375 Assignment 3: K-Means Clustering

This assignment implements the K-means clustering algorithm with the Jaccard distance metric on a sample dataset of health related tweets from the New York Times. The Jaccard distance metric is defined as the difference of the sizes of the union and the intersection of two sets divided by the size of the union of the sets. In this case, each "set" is a tweet represented in a bag of words format. The tweets are preprocessed to remove any special characters and punctuation. The program by default tests the algorithm on 5 different values of k and calculates the SSE for each.

## Execution Instructions

This program runs with `Python 3.9.12` and above.

The following imports are required to run `main.py`:

```python
import numpy as np
import requests
import re
import string
import random
import math
```

Run the program using any acceptable terminal with:

```bash
python main.py
```

## Dataset

The `nytimeshealth.txt` dataset is hosted on our Github repository and can be found at:

```text
https://raw.githubusercontent.com/MertBuyulu/k-means-clustering/main/nytimeshealth.txt
```

The dataset contains `6245` instances/tweets.

## Output

Running the `main.py` file will run the K-means algorithm on 5 values of k and output the SSE and cluster sizes to the terminal. For example:

```text
K = 4
SSE = 5511.9778996771
1 - 310 tweets
2 - 2126 tweets
3 - 1443 tweets
4 - 2366 tweets

K = 6
SSE = 5440.033056238194
1 - 1165 tweets
2 - 1814 tweets
3 - 155 tweets
4 - 2051 tweets
5 - 710 tweets
6 - 350 tweets

K = 8
SSE = 5156.698059849712
1 - 323 tweets
2 - 577 tweets
3 - 516 tweets
4 - 1049 tweets
5 - 513 tweets
6 - 1901 tweets
7 - 620 tweets
8 - 746 tweets

K = 10
SSE = 5132.448962681637
1 - 902 tweets
2 - 1867 tweets
3 - 62 tweets
4 - 516 tweets
5 - 160 tweets
6 - 396 tweets
7 - 499 tweets
8 - 152 tweets
9 - 639 tweets
10 - 1052 tweets

K = 12
SSE = 5077.87964474145
1 - 426 tweets
2 - 2008 tweets
3 - 404 tweets
4 - 187 tweets
5 - 495 tweets
6 - 531 tweets
7 - 50 tweets
8 - 468 tweets
9 - 464 tweets
10 - 282 tweets
11 - 531 tweets
12 - 399 tweets
```

The values of k can be changed from within the main function, and the number of iterations is set to 300 by default but can be raised or lowered in the main function. A lower SSE value signifies better algorithm performance. SSE varies depending on the size of the dataset and the number of clusters (k) and iterations.