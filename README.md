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
SSE = 5050.767820672383
1 - 1483 tweets
2 - 1573 tweets
3 - 2087 tweets
4 - 1102 tweets

K = 6
SSE = 4985.704899150557
1 - 676 tweets
2 - 982 tweets
3 - 1031 tweets
4 - 1693 tweets
5 - 847 tweets
6 - 1016 tweets

K = 8
SSE = 4823.565367902651
1 - 170 tweets
2 - 598 tweets
3 - 675 tweets
4 - 1248 tweets
5 - 614 tweets
6 - 1521 tweets
7 - 912 tweets
8 - 507 tweets

K = 10
SSE = 4800.232817740847
1 - 505 tweets
2 - 769 tweets
3 - 204 tweets
4 - 942 tweets
5 - 88 tweets
6 - 363 tweets
7 - 931 tweets
8 - 881 tweets
9 - 1023 tweets
10 - 539 tweets

K = 12
SSE = 4798.379175879579
1 - 449 tweets
2 - 656 tweets
3 - 362 tweets
4 - 885 tweets
5 - 337 tweets
6 - 329 tweets
7 - 608 tweets
8 - 1432 tweets
9 - 365 tweets
10 - 664 tweets
11 - 61 tweets
12 - 97 tweets
```

The values of k can be changed from within the main function, and the number of iterations is set to 300 by default but can be raised or lowered in the main function. A lower SSE value signifies better algorithm performance. SSE varies depending on the size of the dataset and the number of clusters (k) and iterations.