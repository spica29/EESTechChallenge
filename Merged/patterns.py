import csv
import scipy.integrate as integrate
import math

bags = []
with open('dataLeft.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        value_of_cabine = row['cabine']
        print(value_of_cabine)

f5 = integrate.quad(lambda x: x, min_temp, max_temp)
f6 = math.sqrt(mean)
f7 = numberOfOnes / numberOfZeros