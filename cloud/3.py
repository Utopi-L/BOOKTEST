# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegressionCV
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings


if __name__ == '__main__':
    warnings.filterwarnings(action='ignore')
    #pd.set_option('display.width', 300)
    pd.options.display.width=300
    #pd.set_option('display.max_columns', 300)
    pd.options.display.max_columns=300
    #pd.set_option('max_rows', 100)  # 显示最多行数，超出该数以省略号表示
    pd.options.display.max_rows=100
    data = pd.read_csv('云计算\实验三\car.data', header=None)
    n_columns = len(data.columns)
    columns = ['buy', 'maintain', 'doors', 'persons', 'boot', 'safety', 'accept']
    new_columns = dict(list(zip(np.arange(n_columns), columns)))     # zip打包为元组的列表
    data.rename(columns=new_columns, inplace=True)
    print(data.head(100))
    # print(data.shape)

    # one-hot编码
    x = pd.DataFrame()
    for col in columns[:-1]:
        t = pd.get_dummies(data[col])
        t = t.rename(columns=lambda x: col+'_'+str(x))
        x = pd.concat((x, t), axis=1)
    print(x.head(100))
    # print(x.shape)
    # print (x.columns)
    y = np.array(pd.Categorical(data['accept']).codes)
    # y[y == 1] = 0
    # y[y >= 2] = 1
    # print(np.unique(y))

    x, x_test, y, y_test = train_test_split(x, y, test_size=0.3)
    clf = LogisticRegressionCV(Cs=np.logspace(-3, 4, 8), cv=5,multi_class='auto')
    # clf = RandomForestClassifier(n_estimators= 50, max_depth=7)
    clf.fit(x, y)
    # print(clf.C_)
    y_hat = clf.predict(x)
    print('训练集精确度：', metrics.accuracy_score(y, y_hat))
    y_test_hat = clf.predict(x_test)
    print('测试集精确度：', metrics.accuracy_score(y_test, y_test_hat))
    n_class = len(np.unique(y))