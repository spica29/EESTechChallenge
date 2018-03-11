import csv
import pandas as pd
import math
import numpy as np
import math

data = pd.read_csv('Merged/dataLeft.csv')
#for index, row in dataLeft.iterrows():
#print(dataLeft)
data.index = pd.to_datetime(data['ts'])
#del data['ts']
#print(dataLeft)
data2min = data.resample('2Min')
data2minMin = data2min.max().dropna(how='any')
data2minMax = data2min.max().dropna(how='any')
data2minMean = data2min.mean().dropna(how='any')

data3min = data.resample('3Min')['real_temp']
data3minMin = data3min.min().dropna(how='any').to_frame().reset_index()
data3minMax = data3min.max().dropna(how='any').to_frame().reset_index()
data3minMean = data3min.mean().dropna(how='any').to_frame().reset_index()

data3min = pd.merge(data3minMin, data3minMax, on='ts', how='inner')
data3min = pd.merge(data3min, data3minMean, on='ts', how='inner')
data3min = data3min.rename(index=str, columns={"real_temp_x": "min", "real_temp_y": "max", "real_temp": "mean"})
print(data3min)

data5min = data.resample('5Min')
data5minMin = data5min.min().dropna(how='any')
data5minMax = data5min.max().dropna(how='any')
data5minMean = data5min.mean().dropna(how='any')

data10min = data.resample('10Min')
data10minMin = data10min.min().dropna(how='any')
data10minMax = data10min.max().dropna(how='any')
data10minMean = data10min.mean().dropna(how='any')


