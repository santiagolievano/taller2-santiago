import numpy as np
import pandas as pd

df = pd.read_csv("BikePrices.csv")
print(df.isna().sum())

print("El tamaño del DataFrame es:", df.shape)

print("Las primeras 5 filas del DataFrame son:", df.head())

print("Las últimas 5 filas del DataFrame son:", df.tail())

print("Los tipos de datos de cada columna son:", df.dtypes)

def owner_label(x):
  if x=="1st owner":
    return 1
  elif x=="2nd owner":
    return 3
  elif x=="3rd owner":
    return 4
  else:
    return 5
  
owner_new = df["Owner"].map(owner_label)
print(owner_new)