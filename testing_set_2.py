import pandas as pd
from datetime import datetime

df1 = pd.read_csv("learning_set_2/Log_R3065_CU_BLC_DR_DS.csv")
df2 = pd.read_csv("learning_set_2/Log_R3065_CU_FCU_CV_PV_AS.csv")
df3 = pd.read_csv("learning_set_2/Log_R3065_CU_FCU_HE_PV_AS.csv")
df4 = pd.read_csv("learning_set_2/Log_R3065_CU_GST_INOUT_DS.csv")
df5 = pd.read_csv("learning_set_2/Log_R3065_CU_THS_PV_AS.csv")
df6 = pd.read_csv("learning_set_2/Log_R3065_CU_THS_SP_AS.csv")

date = "2018-01-31"
newdate = datetime.strptime(date, "%Y-%m-%d").date()

df1_filtered = df1[((df1['value'] - 1.79769e+308 < 0.001))]
df2_filtered = df2[((df2['value'] - 1.79769e+308 < 0.001))]
df3_filtered = df3[((df3['value'] - 1.79769e+308 < 0.001))]
df4_filtered = df4[((df4['value'] - 1.79769e+308 < 0.001))]
df5_filtered = df5[((df5['value'] - 1.79769e+308 < 0.001))]
df6_filtered = df6[((df6['value'] - 1.79769e+308 < 0.001))]

#testna mnozica
index_list11= df1_filtered.ts[(df1_filtered.ts < "2018-02-01 00:00:00.00")].index.tolist()
df1_filtered.drop(index_list11, inplace=True)

index_list12= df2_filtered.ts[(df2_filtered.ts < "2018-02-01 00:00:00.00")].index.tolist()
df2_filtered.drop(index_list12, inplace=True)

index_list13= df3_filtered.ts[(df3_filtered.ts < "2018-02-01 00:00:00.00")].index.tolist()
df3_filtered.drop(index_list13, inplace=True)

index_list14= df4_filtered.ts[(df4_filtered.ts < "2018-02-01 00:00:00.00")].index.tolist()
df4_filtered.drop(index_list14, inplace=True)

index_list15= df5_filtered.ts[(df5_filtered.ts < "2018-02-01 00:00:00.00")].index.tolist()
df5_filtered.drop(index_list15, inplace=True)

index_list16= df6_filtered.ts[(df6_filtered.ts < "2018-02-01 00:00:00.00")].index.tolist()
df6_filtered.drop(index_list16, inplace=True)

df1_filtered.to_csv("learning_set_2/testing_set/Log_R3065_CU_BLC_DR_DS_filtered.csv", index=False)
df2_filtered.to_csv("learning_set_2/testing_set/Log_R3065_CU_FCU_CV_PV_AS_filtered.csv", index=False)
df3_filtered.to_csv("learning_set_2/testing_set/Log_R3065_CU_FCU_HE_PV_AS_filtered.csv", index=False)
df4_filtered.to_csv("learning_set_2/testing_set/Log_R3065_CU_GST_INOUT_DS_filtered.csv", index=False)
df5_filtered.to_csv("learning_set_2/testing_set/Log_R3065_CU_THS_PV_AS_filtered.csv", index=False)
df6_filtered.to_csv("learning_set_2/testing_set/Log_R3065_CU_THS_SP_AS_filtered.csv", index=False)