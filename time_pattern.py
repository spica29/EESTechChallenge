import csv
import pandas as pd
import math
import numpy as np
import math
import scipy.integrate as integrate


def integ(array_like):
    #print(array_like)
    #print(data2minMin)
    integ, error = integrate.quad(lambda x: x, data2minMin['real_temp'], data2min['real_temp'])
    return integ

data = pd.read_csv('Merged/dataLeft.csv')
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

    data2minDoorsSum = data2min['balcony'].sum().dropna(how='any').to_frame().reset_index()
    data2minDoorsSum.index = pd.to_datetime(data2minDoorsSum['ts'])
    data2minDoorsLen = data2min['balcony'].size().dropna(how='any').to_frame().reset_index()
    data2minDoorsLen.index = pd.to_datetime(data2minDoorsLen['ts'])

    data2min = data2min['real_temp']
    data2minMin = data2min.min().dropna(how='any').to_frame().reset_index()
    data2minMax = data2min.max().dropna(how='any').to_frame().reset_index()
    data2minMean = data2min.mean().dropna(how='any').to_frame().reset_index()
    data2min = pd.merge(data2minMin, data2minMax, on='ts', how='inner')
    data2min = pd.merge(data2min, data2minMean, on='ts', how='inner')

    data2min = data2min.rename(index=str, columns={"real_temp_x": "min", "real_temp_y": "max", "real_temp": "mean"})
    data2min.index = pd.to_datetime(data2min['ts'])

    for index, row in data2min.iterrows():
        delta_t = data2minRefTempMax.loc[index, 'ref_temp'] - data2minRefTempMin.loc[index, 'ref_temp']
        integ, error = integrate.quad(lambda x: x, data2min.loc[index, 'min'], data2min.loc[index, 'max'])
        rmsd = math.sqrt((data2min.loc[index, 'max'] - data2min.loc[index, 'min']) * (data2min.loc[index, 'max'] - data2min.loc[index, 'min']))
        doors = data2minDoorsSum.loc[index, 'balcony'] / data2minDoorsLen.loc[index, 'balcony']

        data2min.loc[index, 'delta_t'] = delta_t
        data2min.loc[index, 'integ'] = integ
        data2min.loc[index, 'rmsd'] = rmsd
        data2min.loc[index, 'doors'] = doors

    return data2min

data_2 = calculate_test_data(2)
data_3 = calculate_test_data(3)
data_5 = calculate_test_data(5)
data_10 = calculate_test_data(10)

data_2.to_csv("output_2min.csv", sep=',')
data_3.to_csv("output_3min.csv", sep=',')
data_5.to_csv("output_5min.csv", sep=',')
data_10.to_csv("output_10min.csv", sep=',')

