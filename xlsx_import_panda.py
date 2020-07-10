import pandas as pd
xls = pd.ExcelFile('sample.xls')
#print(xls.sheet_names)
df2 = xls.parse('bdonly',skiprows=[0],usecols=[1,5],names=['year','WTFYR'])
print(df2.head())
