import numpy as np

file = 'sample.csv'

digits = np.loadtxt(file,delimiter=',',dtype=float,skiprows=1,usecols=[0])

print(type(digits))
print(digits)

##import mixed data type


d = np.recfromcsv(file)
print(type(d))
print(d[3])
print(d[0:3])
print(d[:3])
print(d['policyID'])
