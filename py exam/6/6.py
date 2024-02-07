import numpy as np
stus_score=np.array([[80,88],[82,81],[84,75],[86,83],[75,81]])
print("每一列的平均值")
result=np.mean(stus_score,axis=0)
print(result)
print("每一行的平均值为:")
result=np.mean(stus_score,axis=1)
print(result)