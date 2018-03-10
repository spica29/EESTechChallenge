import csv
import pandas as pd
import math
import numpy as np
import math

data = pd.read_csv('Merged/dataLeft.csv')
#for index, row in dataLeft.iterrows():
#print(dataLeft)
data.index = pd.to_datetime(data['ts'])
del data['ts']
#print(dataLeft)
data2min = data.resample('2Min')
data2minMin = data2min.max().dropna(how='any')
data2minMax = data2min.max().dropna(how='any')
data2minMean = data2min.mean().dropna(how='any')

data3min = data.resample('3Min')
data3minMin = data3min.min().dropna(how='any')
data3minMax = data3min.max().dropna(how='any')
data3minMean = data3min.mean().dropna(how='any')

data5min = data.resample('5Min')
data5minMin = data5min.min().dropna(how='any')
data5minMax = data5min.max().dropna(how='any')
data5minMean = data5min.mean().dropna(how='any')

data10min = data.resample('10Min')
data10minMin = data10min.min().dropna(how='any')
data10minMax = data10min.max().dropna(how='any')
data10minMean = data10min.mean().dropna(how='any')


