import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
import joblib
# 读入训练数据
print("1.载入训练数据")
trainData = np.loadtxt(open('E:\VS codew\机器学习\实验四\digits_training.csv', 'r'), delimiter=",",skiprows=1)#装载数据
print("2.标准化训练数据")
MTrain, NTrain = np.shape(trainData)  #行列数
xTrain = trainData[:,1:NTrain]
xTrain_col_avg = np.mean(xTrain, axis=0) #对各列求均值
xTrain =(xTrain- xTrain_col_avg)/255  #归一化
yTrain = trainData[:,0]
print("装载训练数据",len(xTrain),"条")

print("3.构建神经网络")
print("4.训练模型")
model = MLPClassifier(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(48, 24))
model.fit(xTrain,yTrain)
print("5.训练完毕,保存模型")
#保存模型
joblib.dump(model,"mlp_classifier_model1.dat")

print("6.模型保存完毕，执行测试...")
print("7.载入测试数据....")
testData = np.loadtxt(open('E:\VS codew\机器学习\实验四\digits_testing.csv', 'r'), delimiter=",",skiprows=1)
MTest,NTest = np.shape(testData)
print("测试集：",MTest,NTest)
print("8.标准化测试数据")
xTest = testData[:,1:NTest]
xTest = (xTest-xTrain_col_avg) /255   # 使用训练数据的列均值进行处理
yTest = testData[:,0]
print("装载测试数据：",len(xTest),"条")
print("9.使用模型进行预测....")
yPredict = model.predict(xTest)
errors = np.count_nonzero(yTest - yPredict) #返回非零项个数
print("预测完毕。错误：", errors, "条")

print("10.评价模型")
print("测试数据正确率:", (MTest - errors) / MTest)
