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
data2minMax = dataLeft.resample('2Min').max()
data3minMax = dataLeft.resample('3Min').max()
data5minMax = dataLeft.resample('5Min').max()
data10minMax = dataLeft.resample('10Min').max()

print(data10minMax)
