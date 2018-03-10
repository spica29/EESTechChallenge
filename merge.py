import csv
import pandas as pd
import math
import numpy as np

refTempR = pd.read_csv('sklop_1/learning_set_2/Log_R3065_CU_THS_SP_AS_filtered.csv')
realTempR = pd.read_csv('sklop_1/learning_set_2/Log_R3065_CU_THS_PV_AS_filtered.csv')
balcDoorR = pd.read_csv('sklop_1/learning_set_2/Log_R3065_CU_BLC_DR_DS_filtered.csv')
cabineR = pd.read_csv('sklop_1/learning_set_2/Log_R3065_CU_GST_INOUT_DS_filtered.csv')

#refTempL = pd.read_csv('learning_set_1/Log_R3063_CU_THS_SP_AS_filtered.csv')
#realTempL = pd.read_csv('learning_set_1/Log_R3063_CU_THS_PV_AS_filtered.csv')
#balcDoorL = pd.read_csv('learning_set_1/Log_R3063_CU_BLC_DR_DS_filtered.csv')
#cabineL = pd.read_csv('learning_set_1/Log_R3063_CU_GST_INOUT_DS_filtered.csv')


#part1 = pd.merge(refTempL, realTempL, on='ts', how='outer')
#part2 = pd.merge(balcDoorL, cabineL, on='ts', how='outer')

part1 = pd.merge(refTempR, realTempR, on='ts', how='outer')
part2 = pd.merge(balcDoorR, cabineR, on='ts', how='outer')

part3 = pd.merge(part1, part2, on='ts', how='outer')

#print(type(c))

value1 = -1
value2 = -1
value3 = -1
value4 = -1

c = part3

c = c.sort_values(by='ts')
#print(c)

for index, row in c.iterrows():
    #print(c.iterrows())
    #print(row['ts'])
    x_x = float(row['value_x_x'])
    y_x = float(row['value_y_x'])
    x_y = float(row['value_x_y'])
    y_y = float(row['value_y_y'])

    #if value is NOT NaN remember the value, if next is NaN it will be replaced with this value
    if math.isnan(x_x) is not True:
        value1 = row['value_x_x']
    else:
        #print("Index " + str(index))
        #print("Old value: ")
        #print(row['value_x'])
        #print("New value: ")
        #print(row['value_x'])
        c.loc[index, 'value_x_x'] = value1

    if math.isnan(y_x) is not True:
        value2 = row['value_y_x']
    else:
        c.loc[index, 'value_y_x'] = value2

    if math.isnan(x_y) is not True:
        value3 = row['value_x_y']
    else:
        c.loc[index, 'value_x_y'] = value3

    if math.isnan(y_y) is not True:
        value4 = row['value_y_y']
    else:
        c.loc[index, 'value_y_y'] = value4

c = c.rename(index=str, columns={"value_x_x": "ref_temp", "value_y_x": "real_temp", "value_x_y": "balcony", "value_y_y": "cabine"})

#c.to_csv("Merged/dataLeft.csv", index=False)
c.to_csv("Merged/dataRight.csv", index=False)