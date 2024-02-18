from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from  sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
sms = pd.read_csv(r'E:\VS codew\机器学习\实验六\messages.csv')
sms_data = sms.iloc[:,0]
sms_label = sms.iloc[:,1]
# 把无意义的符号都替换成空格
sms_data_clear = []
for line in sms_data:
    # 每一行都去掉无意义符号并按空格分词
    for char in line:
        if char.isalpha() is False:
            # 不是字母，发生替换操作:
            newString = line.replace(char," ")
    tempList = newString.split(" ")
    # 将处理好后的一行数据追加到存放干净数据的列表
    sms_data_clear.append(tempList)
# 去掉长度不大于3的词和没有语义的词
sms_data_clear2 = []
for line in sms_data_clear:
    tempList = []
    for word in line:
        if word != '' and len(word) > 3 and word.isalpha():
            tempList.append(word)
    tempString = ' '.join(tempList)
    sms_data_clear2.append(tempString)
sms_data_clear = sms_data_clear2
#划分测试集
print("1读取CSV文件，将数据集按3:1的比例拆分成训练集合测试集")
x_train,x_test,y_train,y_test = train_test_split(sms_data_clear2,sms_label,test_size=0.25,random_state=0,stratify=sms_label)
#词向量化
tfidf = TfidfVectorizer()
X_train = tfidf.fit_transform(x_train)
X_test = tfidf.transform(x_test)
X_train = X_train.toarray()
X_test = X_test.toarray()
X_train.shape
print("2构建词汇表，形成特征矩阵和分类矩阵......")
print("3根据训练数据生成特征矩阵和分类矩阵，显示训练矩阵特征维度......")
print(X_train.shape)
print("4根据测试数据生成特征矩阵和分类矩阵，显示测试矩阵特征维度......")
print(X_test.shape)
# #输出不为0的列
# for i in range(X_train.shape[0]):
#     for j in range(X_train.shape[1]):
#         if X_train[i][j] != 0:
#             print(i,j,X_train[i][j])
#建模
print("5用训练集训练朴素贝叶斯模型......")
mnb = MultinomialNB()
module = mnb.fit(X_train,y_train)
y_predict = module.predict(X_test)
# 输出模型分类的各个指标
print("6用测试集进行预测......")
print("7计算并显示模型的准确率、精度、召回率和F1值......")
from sklearn.metrics import classification_report
cr = classification_report(y_predict,y_test)
print(cr)  

