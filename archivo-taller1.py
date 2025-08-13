import numpy as np
import pandas as pd

df = pd.read_csv("BikePrices.csv")
print(df.isna().sum())

print("El tamaño del DataFrame es:", df.shape)