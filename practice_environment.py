import pandas as pd

df = pd.read_csv('/Users/nicholasglanvill/Documents/GitHub/wbs-pandas/vehicles.csv')

#df.info()


print(df.describe())

print(df.head())

