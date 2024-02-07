import numpy as np
stus_score=np.array([[80,88],[82,81],[84,75],[86,83],[75,81]])
print(np.where(stus_score<80,0,90))