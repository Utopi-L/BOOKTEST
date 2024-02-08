import pandas as pd
import numpy as np
IMDB_1000=pd.read_csv("E:/VS codew/py7/IMDB-Movie-Data.csv")
print(IMDB_1000.dtypes)
IMDB_1000.sort_values(by="Rating",ascending=False)
print("Runtime (Minutes) max:")
print(IMDB_1000[IMDB_1000["Runtime (Minutes)"]==IMDB_1000["Runtime (Minutes)"].max()])
print("Runtime (Minutes) min:")
print(IMDB_1000[IMDB_1000["Runtime (Minutes)"]==IMDB_1000["Runtime (Minutes)"].min()])
print(IMDB_1000["Runtime (Minutes)"].mean())