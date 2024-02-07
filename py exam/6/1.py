import numpy as np
a=[1,2,3,4]
b=np.array(a)
arr=np.random.normal(1.75,0.1,(4,5))
print(arr)
after_arr=arr[1:3,2:4]
print(after_arr)
print("reshape函数的使用!")
one_20=np.ones([20])
print("-->1行20列<--")
print(one_20)
one_4_5=one_20.reshape([4,5])
print("-->4行5列<--")
print(one_4_5)