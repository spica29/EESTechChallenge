import csv
import pandas as pd
import math

df1 = pd.read_csv('C:\\Users\\Amela\\Desktop\\DHmiTrend.db\\Exported\\Log_R3065_CU_THS_SP_AS.csv')
df2 = pd.read_csv('C:\\Users\\Amela\\Desktop\\DHmiTrend.db\\Exported\\Log_R3065_CU_THS_PV_AS.csv')

c = pd.merge(df1,df2,on='ts',how='outer')

print(type(c))

value1 = 0
value2 = 0


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