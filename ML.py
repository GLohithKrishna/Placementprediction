import pandas as pd
df = pd.read_csv('housing.csv', sep=r'\s+', header= None)


print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df.describe())

print(df.duplicated().sum())

