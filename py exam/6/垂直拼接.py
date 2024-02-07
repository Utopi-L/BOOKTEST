from unittest import result
import numpy as np
print("v1为:")
v1=[[0,1,2,3,4,5],
[6,7,8,9,10,11]]
print(v1)
print("v2为:")
v2=[[12,13,14,15,16,17],
[18,19,20,21,22,23]]
print(v2)
result=np.vstack((v1,v2))
print("v1与v2垂直拼接的结果为")
print(result)