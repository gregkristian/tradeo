import sys
import pprint
from matplotlib import pyplot as plt
from sklearn import preprocessing
from util import save_plot

# Read training set
with open('trainingset.txt', 'r') as f:
    data = f.read().splitlines()

print(len(data))
print(type(data))

# save_plot('img1.png', data)

data_normalized = preprocessing.MinMaxScaler().fit_transform(data)

print(len(data_normalized))
print(type(data_normalized))
