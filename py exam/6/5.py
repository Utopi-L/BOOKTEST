import numpy as np
stus_score=np.array([[80,88],[82,81],[84,75],[86,83],[75,81]])
print("每一列的最小值")
result=np.amin(stus_score,axis=0)
print(result)
print("每一行的最小值为:")
result=np.amin(stus_score,axis=1)
print(result)