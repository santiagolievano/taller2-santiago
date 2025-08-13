import numpy as np
import pandas as pd

df = pd.read_csv("BikePrices.csv")
print(df.isna().sum())

print("El tamaño del DataFrame es:", df.shape)

print("Las primeras 5 filas del DataFrame son:", df.head())

print("Las últimas 5 filas del DataFrame son:", df.tail())

print("Los tipos de datos de cada columna son:", df.dtypes)