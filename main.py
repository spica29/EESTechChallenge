import csv
import pandas as pd
import datetime as datetime
import os

df1 = pd.read_csv('C:\\Users\\Amela\\Desktop\\DHmiTrend.db\\Exported\\Log_R3065_CU_THS_SP_AS.csv')
df2 = pd.read_csv('C:\\Users\\Amela\\Desktop\\DHmiTrend.db\\Exported\\Log_R3065_CU_THS_PV_AS.csv')
df3 = open('C:\\Users\\Amela\\Desktop\\DHmiTrend.db\\Exported\\newFile.csv')
filewriter = csv.writer(df3, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

i = 0
j = 0
counter = 0
while i < len(df1) - 1:
    while j < len(df2) - 1:
        if df1[i][0] == df2[i]:
            list[counter] = [df1[i][0], df1[i][1], df2[j][1]]
            i = i + 1
            j = j + 1
        elif i + 1 < j + 1:
            list[counter] = [df1[i+1][0], df1[i+1][1], df2[j][1]]
            i = i + 1
            j = j + 1


counter = 0
for key1, value1 in df1.items():
    for key2, value2 in df2.items():
        if key1 >= key2:
            listOfKeysToDelete = listOfKeysToDelete + key2
            filewriter.writerow([key1, value1, value2])
        else:
            break
    df3.pop(listOfKeysToDelete, None)


    #for key2, value2 in df2.items():
     #   if key1 == key2:
       #     df3.write(key1 + value1 + value2)
      #  elif key1 > key2:
        #    df3.write(key1, value1, value2)
        #elif key2 > key1:
        #    df3.write(key1, value1, value2)




print str(df1)
print str(df2)