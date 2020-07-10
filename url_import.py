from urllib.request import urlretrieve

import pandas as pd

urlretrieve('https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv', 'wine.csv')
df = pd.read_csv('wine.csv',sep=';')
print(df.head())


