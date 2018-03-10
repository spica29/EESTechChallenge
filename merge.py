import csv
import pandas as pd
import math
import numpy as np

refTempR = pd.read_csv('learning_set_1/Log_R3063_CU_THS_SP_AS_filtered.csv')
realTempR = pd.read_csv('learning_set_1/Log_R3065_CU_THS_PV_AS_filtered.csv')
balcDoorR = pd.read_csv('learning_set_1/Log_R3065_CU_BLC_DR_DS_filtered.csv')
cabineR = pd.read_csv('learning_set_1/Log_R3065_CU_GST_INOUT_DS_filtered.csv')

refTempL = pd.read_csv('learning_set_1/Log_R3063_CU_THS_SP_AS_filtered.csv')
realTempL = pd.read_csv('learning_set_1/Log_R3063_CU_THS_PV_AS_filtered.csv')
balcDoorL = pd.read_csv('learning_set_1/Log_R3063_CU_BLC_DR_DS_filtered.csv')
cabineL = pd.read_csv('learning_set_1/Log_R3063_CU_GST_INOUT_DS_filtered.csv')


part1 = pd.merge(refTempR, realTempR, on='ts', how='outer')
part2 = pd.merge(balcDoorR, cabineR, on='ts', how='outer')

part3 = pd.merge(part1, part2, on='ts', how='outer')

#print(type(c))

value1 = 0
value2 = 0

c = part3

for index, row in c.iterrows():
    #print(c.iterrows())

    x = float(row['value_x'])
    y = float(row['value_y'])

    #if value is NOT NaN remember the value, if next is NaN it will be replaced with this value
    if math.isnan(x) is not True:
        value1 = row['value_x']
    else:
        #print("Index " + str(index))
        #print("Old value: ")
        #print(row['value_x'])
        #print("New value: ")
        #print(row['value_x'])
        c.loc[index, 'value_x'] = value1

    if math.isnan(y) is not True:
        value2 = row['value_y']
    else:
        c.loc[index, 'value_y'] = value2


print(c)

c.to_csv("data", index=False)