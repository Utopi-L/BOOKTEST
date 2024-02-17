from sklearn.neural_network import MLPClassifier
from sklearn.decomposition import PCA
import numpy
import pandas
import joblib
print("1.载入训练数据，对自变量进行标准化，输出训练数据的样本数……")
trainData = pandas.read_csv("E:\VS codew\机器学习\实验五\digits_training.csv")
xTrain = trainData.values[:,1:]
yTrain = trainData.values[:,0]
def normalizeData(X):
    return X- numpy.mean(X,axis=0)
xTrain = normalizeData(xTrain)
print('装载训练数据: {0} 条'.format(xTrain.shape[0]))
# PCA数据降维
print('2.使用PCA对数据降维，取累积贡献率超过98%的前K个元素……')
pca = PCA(n_components=0.98,svd_solver='full')
# print(pca.n_components)
xTrain = pca.fit_transform(xTrain)
# print(newX)
print("选取了 {}个主成分".format(xTrain.shape[1]))
print("训练数据维度:{}".format(xTrain.shape))
print("3.使用神经网络（多层感知机）训练分类模型")
# 构建模型
mpl = MLPClassifier(solver="lbfgs",alpha=1e-5,hidden_layer_sizes=(48,24),random_state=1,max_iter=10000)
# 训练模型
mpl.fit(xTrain,yTrain)
print("4.保存分类模型……")
joblib.dump(mpl,'mlpNN_pca.m')
print("5.载入测试数据，对自变量进行标准化，输出测试数据的样本数……")
testData = pandas.read_csv("E:\VS codew\机器学习\实验五\digits_testing.csv")
xTest = testData.values[:,1:]
yTest = testData.values[:,0]
xTest = normalizeData(xTest)
xTest = pca.transform(xTest)
print('测试数据维度：{}'.format(xTest.shape))
print("6.使用模型对测试数据分类……")
model = joblib.load('mlpNN_pca.m')
equal = model.predict(xTest)
print("输出模型准确率……")
print("错误：",(equal!=yTest).sum())
print("测试数据准确率：",(equal==yTest).sum()/len(yTest))

