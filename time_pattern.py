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
data2min = data.resample('2Min')['real_temp']
data2minMin = data2min.min().dropna(how='any').to_frame().reset_index()
data2minMax = data2min.max().dropna(how='any').to_frame().reset_index()
data2minMean = data2min.mean().dropna(how='any').to_frame().reset_index()
data2minDelta = list(map(max, data2min))

print(data2minDelta)
data2min = pd.merge(data2minMin, data2minMax, on='ts', how='inner')
data2min = pd.merge(data2min, data2minMean, on='ts', how='inner')
#data2min = pd.merge(data2min, data2minDelta, on='ts', how='inner')
data2min = data2min.rename(index=str, columns={"real_temp_x": "min", "real_temp_y": "max", "real_temp": "mean"})
#print(data2min)

data3min = data.resample('3Min')['real_temp']
data3minMin = data3min.min().dropna(how='any').to_frame().reset_index()
data3minMax = data3min.max().dropna(how='any').to_frame().reset_index()
data3minMean = data3min.mean().dropna(how='any').to_frame().reset_index()

data3min = pd.merge(data3minMin, data3minMax, on='ts', how='inner')
data3min = pd.merge(data3min, data3minMean, on='ts', how='inner')
data3min = data3min.rename(index=str, columns={"real_temp_x": "min", "real_temp_y": "max", "real_temp": "mean"})
#print(data3min)

data5min = data.resample('5Min')['real_temp']
data5minMin = data5min.min().dropna(how='any').to_frame().reset_index()
data5minMax = data5min.max().dropna(how='any').to_frame().reset_index()
data5minMean = data5min.mean().dropna(how='any').to_frame().reset_index()

data5min = pd.merge(data5minMin, data5minMax, on='ts', how='inner')
data5min = pd.merge(data5min, data5minMean, on='ts', how='inner')
data5min = data5min.rename(index=str, columns={"real_temp_x": "min", "real_temp_y": "max", "real_temp": "mean"})
#print(data5min)

data10min = data.resample('10Min')['real_temp']
data10minMin = data10min.min().dropna(how='any').to_frame().reset_index()
data10minMax = data10min.max().dropna(how='any').to_frame().reset_index()
data10minMean = data10min.mean().dropna(how='any').to_frame().reset_index()
data10minMean = data10min.mean().dropna(how='any').to_frame().reset_index()

data10min = pd.merge(data10minMin, data10minMax, on='ts', how='inner')
data10min = pd.merge(data10min, data10minMean, on='ts', how='inner')
data10min = data10min.rename(index=str, columns={"real_temp_x": "min", "real_temp_y": "max", "real_temp": "mean"})
#print(data10min)
