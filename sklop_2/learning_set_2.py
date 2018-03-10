import pandas as pd
from datetime import datetime

df1 = pd.read_csv("learning_set_2/Log_R3065_CU_FCU_CV_PV_AS.csv")
df4 = pd.read_csv("learning_set_2/Log_R3065_CU_FCU_HE_PV_AS.csv")

date = "2018-01-31"
newdate = datetime.strptime(date, "%Y-%m-%d").date()

#ucna mnozica
df1_filtered = df1[((df1['value'] - 1.79769e+308 < 0.001))]
df4_filtered = df4[((df4['value'] - 1.79769e+308 < 0.001))]

index_list1= df1_filtered.ts[(df1_filtered.ts >= "2018-02-01 00:00:00.00")].index.tolist()
df1_filtered.drop(index_list1, inplace=True)

index_list4= df4_filtered.ts[(df4_filtered.ts >= "2018-02-01 00:00:00.00")].index.tolist()
df4_filtered.drop(index_list4, inplace=True)

df1_filtered.to_csv("learning_set_2/Log_R3065_CU_FCU_CV_PV_AS_filtered.csv", index=False)
df4_filtered.to_csv("learning_set_2/Log_R3065_CU_FCU_HE_PV_AS_filtered.csv", index=False)
