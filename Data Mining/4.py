#200511437 黄思伟

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.naive_bayes import GaussianNB

# 读取数据集
data = pd.read_csv("//实验4-Data_User_Modeling_Dataset_Hamdi Tolga KAHRAMAN.csv")
# 分离特征和标签
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 创建朴素贝叶斯分类器
gnb = GaussianNB()
# 训练模型
gnb.fit(X_train, y_train)
# 预测测试集
y_pred = gnb.predict(X_test)
# 计算准确度
accuracy = (y_pred == y_test).sum() / len(y_test)
print("准确度：", accuracy)
# 输出混淆矩阵和分类报告
print("混淆矩阵：\n", confusion_matrix(y_test, y_pred))
print("分类报告：\n", classification_report(y_test, y_pred))
