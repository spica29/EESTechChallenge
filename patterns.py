import csv
import pandas as pd
import math
import numpy as np

dataLeft = pd.read_csv('Merged/dataLeft.csv')
changed = False
for index, row in dataLeft.iterrows():
    listOfPatterns = []
    listOfTemperatures = []
    while changed is False:
        # check if cabine value has changed
        if index > 0:
            if dataLeft.loc[index, 'cabine'] != dataLeft.loc[index-1, 'cabine']:
                changed = True
                break
            else:
                changed = False
        #write all elements to one list
        listOfPatterns.append(dataLeft.loc[index])
        listOfTemperatures.append(dataLeft.loc[index, 'real_temp'])

        index = index + 1
    print("list of temperatures")
    print(listOfTemperatures)
    #calculate min
    min_temp = min(listOfTemperatures)

