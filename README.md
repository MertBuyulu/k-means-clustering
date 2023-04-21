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
SSE = 5511.977899677199
1 - 2127 tweets
2 - 2369 tweets
3 - 308 tweets
4 - 1441 tweets

K = 6
SSE = 5312.693067914187
1 - 1804 tweets
2 - 1150 tweets
3 - 792 tweets
4 - 689 tweets
5 - 128 tweets
6 - 1682 tweets

K = 8
SSE = 5266.142718546209
1 - 1162 tweets
2 - 75 tweets
3 - 268 tweets
4 - 696 tweets
5 - 2443 tweets
6 - 351 tweets
7 - 635 tweets
8 - 615 tweets

K = 10
SSE = 5092.777759487703
1 - 1802 tweets
2 - 628 tweets
3 - 575 tweets
4 - 591 tweets
5 - 880 tweets
6 - 465 tweets
7 - 462 tweets
8 - 426 tweets
9 - 349 tweets
10 - 67 tweets

K = 12
SSE = 5091.109270539705
1 - 851 tweets
2 - 2014 tweets
3 - 414 tweets
4 - 479 tweets
5 - 370 tweets
6 - 154 tweets
7 - 468 tweets
8 - 502 tweets
9 - 103 tweets
10 - 58 tweets
11 - 536 tweets
12 - 296 tweets
```

The values of k can be changed from within the main function, and the number of iterations is set to 300 by default but can be raised or lowered in the main function. A lower SSE value signifies better algorithm performance. SSE varies depending on the size of the dataset and the number of clusters (k) and iterations.