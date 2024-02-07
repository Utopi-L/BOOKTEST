import numpy as np
stus_score=np.array([[80,88],[82,81],[84,75],[86,83],[75,81]])
print("减半前:")
print(stus_score)
stus_score[:,0]=stus_score[:,0]*0.5
print("减半后:")
print(stus_score)