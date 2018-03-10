import csv
import pandas as pd
import math
import numpy as np
import scipy.integrate as integrate
import math

dataLeft = pd.read_csv('Merged/dataLeft.csv')
#for index, row in dataLeft.iterrows():
index = 0
listOfTemperatures = []
listOfRelTemperatures = []
listBalcony = []

listOfVectors = []
while index < len(dataLeft):
    sample = []
    listOfPatterns = []
    changed = False
    while changed is False:
        # check if cabine value has changed
        if index > 0 & index < len(dataLeft):
            if dataLeft.loc[index, 'cabine'] != dataLeft.loc[index - 1, 'cabine']:
                changed = True
                break

        #write all elements to one list
        #listOfPatterns.append(dataLeft.loc[index])
        listBalcony.append(dataLeft.loc[index, 'balcony'])
        listOfTemperatures.append(dataLeft.loc[index, 'real_temp'])
        listOfRelTemperatures.append(dataLeft.loc[index, 'ref_temp'])

        if index >= (len(dataLeft) - 1):
            break
        if index <= len(dataLeft):
            index = index + 1

    #normalize data
    newlistOfTemperatures = []
    newlistOfRelTemperatures = []
    for i in range(0, len(listOfTemperatures)):
        a = listOfTemperatures[i] / 26
        newlistOfTemperatures.append(a)
        b = listOfRelTemperatures[i] / 26
        newlistOfRelTemperatures.append(b)

    #calculate delta_t
    delta_t = max(newlistOfRelTemperatures) - min(newlistOfRelTemperatures)
    #calculate min
    min_temp = min(newlistOfTemperatures)
    #print(min_temp)
    #calculate max
    max_temp = max(newlistOfTemperatures)
    #calculate mean
    mean = sum(newlistOfTemperatures) / len(newlistOfTemperatures)
    #calculate integral
    integ, error = integrate.quad(lambda x: x, min_temp, max_temp)
    #calculate root mean square deviation
    rmsd = math.sqrt((max_temp - min_temp)*(max_temp - min_temp))
    #delez odprtosti balkonskih vrat
    number_of_doors = 0
    for i in range(0, len(listBalcony)):
        if (listBalcony[i] == 1):
            number_of_doors += 1
    doors = number_of_doors/len(listBalcony)

    sample.append(delta_t)
    sample.append(min_temp)
    sample.append(max_temp)
    sample.append(mean)
    sample.append(integ)
    sample.append(rmsd)
    sample.append(doors)
    sample.append(dataLeft.loc[index-1, 'cabine'])

    listOfVectors.append(sample)

    listBalcony = []
    listBalcony.append(dataLeft.loc[index, 'balcony'])
    listOfRelTemperatures = []
    listOfRelTemperatures.append(dataLeft.loc[index, 'ref_temp'])
    listOfTemperatures = []
    listOfTemperatures.append(dataLeft.loc[index, 'real_temp'])

    if index < len(dataLeft):
        index = index + 1


for i in range(0, len(listOfVectors)):
    print(listOfVectors[i])

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(listOfVectors)

