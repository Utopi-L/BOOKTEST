from sklearn import datasets
import numpy as np

#获取data和类标
iris = datasets.load_iris()
X = iris.data[:,[2,3]]
y = iris.target

#测试样本和训练样本三七分
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)

#数据特征标准化
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_test_std = sc.transform(X_test)
X_train_std = sc.transform(X_train)

#训练感知器模型
from sklearn.linear_model import Perceptron
ppn = Perceptron(max_iter=40,eta0=0.1,random_state=0)
ppn.fit(X_train_std,y_train)

#训练完成后，对测试数据进行预测
y_pred = ppn.predict(X_test_std)
print('Missclassified samples:%d'%(y_pred!=y_test).sum())
from sklearn.metrics import accuracy_score
print('Accuracy:%.10f'%accuracy_score(y_test,y_pred))