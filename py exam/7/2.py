import pandas as pd
import numpy as np
result=pd.read_csv("E:/VS codew/py7/students_score.csv")
print(result)
print(result["姓名"][0:6])
print("读取后返回的数据类型为-->",type(result))
print(result[result["age"]>23])