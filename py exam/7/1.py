import pandas as pd
import numpy as np
result=pd.read_csv("E:/VS codew/py7/students_score.csv")
print(result.shape)
print(result.dtypes)
print(result.ndim)
print(result.index)
print(result.columns)
print(result.values)
print("-->前五个<--")
print(result.head(5))
print("-->后五个<--")
print("-->描述信息:")
print(result.describe())