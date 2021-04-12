import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler

from util import save_plot

# Read csv. Use Open and High (col 1 & 2) to predict Close price (col 4). Normalize
dataset_df = pd.read_csv("dataset.csv")

print(dataset_df.head())

training_set = dataset_df.iloc[:800, 1:2].values
test_set = dataset_df.iloc[800:, 1:2].values

sc = MinMaxScaler(feature_range = (0, 1))
training_set_norm = sc.fit_transform(training_set)
test_set_norm = sc.fit_transform(test_set)

#print(training_set_norm.head())
#print(test_set_norm.head())

#data = data[:1000]
# print(len(data))

#plt.plot(data)
#plt.show()
# save_plot('img1.png', data)

# data_normalized = preprocessing.

# print(len(data_normalized))
# print(type(data_normalized))
