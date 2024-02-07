from unittest import result
import numpy as np
from sklearn.utils import resample
stus_score=np.array([[80,88],[82,81],[84,75],[86,83],[75,81]])
q=np.array([[0.4],[0.6]])
result=np.dot(stus_score,q)
print("最终结果为:")
print(result)