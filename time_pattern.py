import csv
import pandas as pd
import math
import numpy as np
import math
import scipy.integrate as integrate

data = pd.read_csv('Merged/dataRight.csv')
data.index = pd.to_datetime(data['ts'])

def custom_function(array):
    return array

def calculate_test_data(interval):

    if (interval == 2):
        data2min = data.resample('2Min')
    elif (interval == 3):
        data2min = data.resample('3Min')
    elif (interval == 5):
        data2min = data.resample('5Min')
    elif (interval == 10):
        data2min = data.resample('10Min')

    #print(data2min['real_temp'])
    data2minRefTemp = data2min['ref_temp']
    data2minRefTempMin = data2minRefTemp.min().dropna(how='any').to_frame().reset_index()
    data2minRefTempMax = data2minRefTemp.max().dropna(how='any').to_frame().reset_index()
    data2minRefTempMin.index = pd.to_datetime(data2minRefTempMin['ts'])
    data2minRefTempMax.index = pd.to_datetime(data2minRefTempMax['ts'])

    cabine = data2min['cabine'].max().to_frame().reset_index()
    cabine.index = pd.to_datetime(cabine['ts'])
    #print(cabine)

    data2minDoorsSum = data2min['balcony'].sum().dropna(how='any').to_frame().reset_index()
    data2minDoorsSum.index = pd.to_datetime(data2minDoorsSum['ts'])
    data2minDoorsLen = data2min['balcony'].size().dropna(how='any').to_frame().reset_index()
    data2minDoorsLen.index = pd.to_datetime(data2minDoorsLen['ts'])

    data2min = data2min['real_temp']
    data2minMin = data2min.min().dropna(how='any').to_frame().reset_index()
    data2minMin.index = pd.to_datetime(data2minMin['ts'])
    data2minMax = data2min.max().dropna(how='any').to_frame().reset_index()
    data2minMax.index = pd.to_datetime(data2minMax['ts'])
    data2minMean = data2min.mean().dropna(how='any').to_frame().reset_index()
    #data2min = pd.merge(data2minMin, data2minMax, on='ts', how='inner')
    #data2min = pd.merge(data2min, data2minMean, on='ts', how='inner')
    data2min = data2minMean
    #data2min = data2min.rename(index=str, columns={"real_temp_x": "min", "real_temp_y": "max", "real_temp": "mean"})
    data2min.index = pd.to_datetime(data2min['ts'])

    for index, row in data2min.iterrows():
        min = data2minMin.loc[index, 'real_temp'] / 26
        max = data2minMax.loc[index, 'real_temp'] / 26
        mean = data2minMean.loc[index, 'real_temp'] / 26
        delta_t = data2minRefTempMax.loc[index, 'ref_temp'] - data2minRefTempMin.loc[index, 'ref_temp']
        integ, error = integrate.quad(lambda x: x, min, max)
        rmsd = math.sqrt((max - min) * (max - min))
        doors = data2minDoorsSum.loc[index, 'balcony'] / data2minDoorsLen.loc[index, 'balcony']

        cabineOcc = cabine.loc[index, 'cabine']

        data2min.loc[index, 'min'] = min
        data2min.loc[index, 'max'] = max
        data2min.loc[index, 'mean'] = mean
        data2min.loc[index, 'delta_t'] = delta_t
        data2min.loc[index, 'integ'] = integ
        data2min.loc[index, 'rmsd'] = rmsd
        data2min.loc[index, 'doors'] = doors
        data2min.loc[index, 'cabine'] = cabineOcc

    return data2min

data_2 = calculate_test_data(2)
data_3 = calculate_test_data(3)
data_5 = calculate_test_data(5)
data_10 = calculate_test_data(10)

#data_2.to_csv("output_2min_left.csv", sep=',')
#data_3.to_csv("output_3min_left.csv", sep=',')
#data_5.to_csv("output_5min_left.csv", sep=',')
#data_10.to_csv("output_10min_left.csv", sep=',')

data_2.to_csv("output_2min_right.csv", sep=',')
data_3.to_csv("output_3min_right.csv", sep=',')
data_5.to_csv("output_5min_right.csv", sep=',')
data_10.to_csv("output_10min_right.csv", sep=',')

