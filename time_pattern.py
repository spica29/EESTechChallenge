import csv
import pandas as pd
import math
import numpy as np
import math

dataLeft = pd.read_csv('Merged/dataLeft.csv')
#for index, row in dataLeft.iterrows():
#print(dataLeft)
dataLeft.index = pd.to_datetime(dataLeft['ts'])
del dataLeft['ts']
#print(dataLeft)
data2minMax = dataLeft.resample('2Min').max().dropna(how='any')
data3minMax = dataLeft.resample('3Min').max().dropna(how='any')
data5minMax = dataLeft.resample('5Min').max().dropna(how='any')
data10minMax = dataLeft.resample('10Min').max().dropna(how='any')

data2minMin = dataLeft.resample('2Min').min().dropna(how='any')
data3minMin = dataLeft.resample('3Min').min().dropna(how='any')
data5minMin = dataLeft.resample('5Min').min().dropna(how='any')
data10minMin = dataLeft.resample('10Min').min().dropna(how='any')

