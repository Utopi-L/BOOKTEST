
import pandas as pd
from pyspark.mllib.recommendation import ALS
# from pyspark.sql import SparkSession
from pyspark import SparkContext
import math
import warnings
import os
#os.environ['JAVA_HOME'] = 'F:\Program Files\JAVA1.8\JDK1.8_0351'

warnings.filterwarnings('ignore')
# pip install pyspark -i https://mirrors.aliyun.com/pypi/simple/

print("1.加载评分文件……")
# spark = SparkSession.builder.master('local').appName("test_script").getOrCreate()
sc = SparkContext()
# sc.setLogLevel("ERROR")
small_raw_data = sc.textFile(os.path.normpath('E:/VS CodeW/机器学习/实验八/ratings.csv'))
small_data = small_raw_data.map(lambda line: line.split(",")).map(lambda col:(col[0],col[1],col[2]))

print("2.按照6：2：2分为训练集、验证集、测试集……")
training_RDD,validation_RDD,test_RDD = small_data.randomSplit([6,2,2],seed=10)
validation_predict_RDD = validation_RDD.map(lambda x:(x[0],x[1]))
test_predict_RDD = test_RDD.map(lambda x:(x[0],x[1]))

print("3. 设置协同过滤推荐算法ALS(交替最小二乘法)参数……")
min_error = float('inf')
best_rank = 1
best_iteration =-1
regularization_param = 0.3
iterations = 10
seed = 10
ranks = [4,8,12]
errors = [0,0,0]
err = 0
for rank in ranks:
    model = ALS.train(training_RDD,rank,seed= 10,iterations=10,lambda_ =0.3)
    predict = model.predictAll(validation_predict_RDD).map(lambda r:((r[0]),r[1],r[2]))
    rate_pre = validation_RDD.map(lambda r:((int(r[0]),int(r[1])),float(r[2]))).join(predict)
    error = math.sqrt(rate_pre.map(lambda r:(r[1][0] - r[1][1])**2).mean())
    errors[err] = error
    err+= 1
    if error <min_error:
        min_error = error
        best_rank = rank

print("4.训练模型，确认最佳的秩（rank）,确认最小误差……")
print("最佳秩值：", best_rank)
print("最小的误差：",min_error)
print("5.用最佳秩重新训练模型……")
model = ALS.train(training_RDD,best_rank,seed=seed,iterations=iterations,
                  lambda_ =regularization_param)
# 保存模型
# model.save(sc,"spark_movie.model")
# sameModel = MatrixFactorizationModel.load(sc,"spark_movie.model")
print("6.使用测试集对模型进行测试……")
predictions = model.predictAll(test_predict_RDD).map(lambda r: ((r[0],r[1]),r[2]))
rates_p = test_RDD.map(lambda r: ((int(r[0]),int(r[1])),float(r[2]))).join(predictions)
error = math.sqrt(rates_p.map(lambda r:(r[1][0]-r[1][1])** 2).mean())
print('REMS = %s '%error)

print("7.计算测试集最小误差……")
print("测试集最小误差RMSE=",error)

print("8.预测用户对电影的评分……")
user_id = 189
movie_id = 2598
predictedRating = model.predict(user_id,movie_id)
print("用户编号：",user_id,"对电影：",movie_id,"的评分为：",predictedRating)

print("9.向某一用户推荐10部电影：")
user_id = 385
topKRecs = model.recommendProducts(user_id ,10)
print("向用户编号：",user_id,"的用户推荐10部电影：")
for rec in topKRecs:
     print(rec)
