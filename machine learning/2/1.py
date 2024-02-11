import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder

#题目一：读入数据并显示数据的维度和前五行数据
print('1.载入数据.....')
data = pd.read_csv("E:\VS codew\机器学习\实验二\income_classification.csv", header=0)
print('数据的维度和前五行数据：', data.shape)
print(data.head())

print('对连续变量age进行离散化处理，等宽分成五类，显示前五行：')
AGE_CUT = pd.cut(x=data['age'], bins=5, labels=range(0, 5))
data['age'] = AGE_CUT
print(data.head(5))
class_le = LabelEncoder()
data['workclass'] = pd.DataFrame(class_le.fit_transform(data['workclass']))
data['marital-status'] = pd.DataFrame(class_le.fit_transform(data['marital-status']))
data['occupation'] = pd.DataFrame(class_le.fit_transform(data['occupation']))
data['education'] = pd.DataFrame(class_le.fit_transform(data['education']))
data['native-country'] = pd.DataFrame(class_le.fit_transform(data['native-country']))
data['relationship'] = pd.DataFrame(class_le.fit_transform(data['relationship']))
data['race'] = pd.DataFrame(class_le.fit_transform(data['race']))
data['sex'] = pd.DataFrame(class_le.fit_transform(data['sex']))
print('显示前五行编码后的结果：')
print(data.head(5))

data1 = []
labels = []
for index, row in data.iterrows():
    # data需要是字典形式，因为之后需要使用DictVectorizer()修改字符串数据类型，以便符合DecisionTreeClassifier()
    rowDict = {}
    row = list(row)
    rowDict['age'] = row[0]
    rowDict['workclass'] = row[1]
    rowDict['education'] = row[2]
    rowDict['education_num'] = row[3]
    rowDict['maritial_status'] = row[4]
    rowDict['occupation'] = row[5]
    rowDict['relationship'] = row[6]
    rowDict['race'] = row[7]
    rowDict['sex'] = row[8]
    rowDict['capital_gain'] = row[9]
    rowDict['capital_loss'] = row[10]
    rowDict['hours_per_week'] = row[11]
    rowDict['native_country'] = row[12]
    data1.append(rowDict)
    labels.append(row[-1])

print('2. 构造数据和标签.....')
x = np.array(data1)
labels = np.array(labels)
y = np.zeros(labels.shape)  # 初始label全为0
y[labels == '<=50K'] = 0  # 当label等于这三种属性的话，设置为1。
y[labels == '>50K'] = 1

# 转换字符串数据类型
print('3.转换字符串数据类型.....')
vec = DictVectorizer()
dx = vec.fit_transform(x).toarray()

# 拆分成训练数据和测试数据
print('4.拆分训练数据和测试数据.....')
print('训练集和验证集比例7:3')
ratio = 0.7
xTrain = []
yTrain = []
xTest = []
yTest = []
features = xTrain, xTest
labels = yTrain, yTest
for i in range(len(dx)):
    dataSetIndex = 0 if np.random.random() < ratio else 1
    features[dataSetIndex].append(dx[i])
    labels[dataSetIndex].append(y[i])

# CART决策树分类
print('5.CART决策树分类.....')
clf_cart = tree.DecisionTreeClassifier(criterion='entropy')  # CART算法，使用entropy作为标准；默认是是用gini作为标准
clf_cart.fit(xTrain, yTrain)

# 检查准确率
accuracy_cart = clf_cart.score(xTest, yTest)
print('CART树分类准确率：', accuracy_cart)

print('6.随机森林分类.....')
clf_random = RandomForestClassifier()
clf_random.fit(xTrain, yTrain)

# 检查准确率
accuracy_random = clf_random.score(xTest, yTest)
print('随机森林分类准确率：', accuracy_random)

