import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

lm =LinearRegression() #构建线性模型

x_train = [[6], [8], [10], [14], [18]]

y_train = [[7], [9], [13], [17.5], [18]]

x_test = [[8], [9], [11], [12], [16]]

y_test = [[8.5], [11], [12], [15], [18]]

lm.fit(x_train, y_train)#训练模型
plt.scatter(x_train,y_train,color='green')
plt.title('')
plt.show()

plt.scatter(x_train, y_train, color='green')

plt.plot(x_train, lm.predict(x_train), color='red', linewidth=4) #画出回归直线

plt.xlabel('Diam')

plt.ylabel('Price')

plt.title('TestImg ')

plt.show()
lm.fit(x_train,y_train)
k=lm.coef_
b=lm.intercept_
print("截距：",b)
print("斜率：",k)

plt.scatter(x_test, y_test, color='green')

plt.plot(x_test, lm.predict(x_test), color='red', linewidth=4) #画出回归直线

plt.xlabel('Diam')

plt.ylabel('Price')

plt.title('PredictImg ')

plt.show()

PredictPrice = lm.predict([[12]])

print('twelve inch pizza price %d' % PredictPrice)

print('model score = ', lm.score(x_test, y_test))