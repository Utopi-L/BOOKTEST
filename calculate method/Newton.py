import math
import numpy as np
import sympy
from sympy import *

x = symbols("x")
x_value=[]
x_iteration=[]
x_diff_iteration=[]


def function_value():
    return x*x*x-x-1

def Newton_Methods(x0,f):  #此处x0为初值,f为函数方程
    k=0                    #记录迭代次数
    x_value.append(x0)
    x_iteration.append(f.subs(x,x0))
    x_diff_iteration.append(diff(f,x).subs(x,x0))
    while(k<10):            #小于规定迭代次数
        x_value.append(x_value[k]-(x_iteration[k]/x_diff_iteration[k]))
        x_iteration.append(f.subs(x,x_value[k+1]))
        x_diff_iteration.append(diff(f,x).subs(x,x_value[k+1]))
        #if(x_iteration[-1]==x_iteration[-2]):    #终止迭代条件
         #   break
        k=k+1
    return x_value


result=Newton_Methods(1.5,function_value())

#格式化输出
for i in range(len(result)):
    print('When k=%d,the x value is %.10f'%(i,result[i]))
