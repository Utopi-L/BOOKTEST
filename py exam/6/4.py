from unittest import result
from matplotlib.pyplot import axis
import numpy as np
stus_score=np.array([[80,88],[82,81],[84,75],[86,83],[75,81]])
print("每一列的最大值")
result=np.amax(stus_score,axis=0)
print(result)
print("每一行的最大值为:")
result=np.max(stus_score,axis=1)
print(result)