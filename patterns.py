import csv
import pandas as pd
import math
import numpy as np

dataLeft = pd.read_csv('Merged/dataLeft.csv')
#for index, row in dataLeft.iterrows():
index = 0
listOfTemperatures = []
print("size " + str(len(dataLeft)))
while index < len(dataLeft):
    listOfPatterns = []
    changed = False
    while changed is False:
        # check if cabine value has changed
        print("index in if" + str(index) + "value " + str(dataLeft.loc[index, 'real_temp']))
        if index > 0 & index < len(dataLeft):
            if dataLeft.loc[index, 'cabine'] != dataLeft.loc[index - 1, 'cabine']:
                changed = True
                break

        #write all elements to one list
        listOfPatterns.append(dataLeft.loc[index])
        listOfTemperatures.append(dataLeft.loc[index, 'real_temp'])
        if index >= (len(dataLeft) - 1):
            break
        if index <= len(dataLeft):
            index = index + 1

    print("index " + str(index))
    print("list of temperatures")
    print(listOfTemperatures)
    #calculate min
    min_temp = min(listOfTemperatures)
    print(min_temp)

    listOfTemperatures = []
    listOfTemperatures.append(dataLeft.loc[index, 'real_temp'])

    if index < len(dataLeft):
        index = index + 1


