import pandas as pd
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
data = pd.read_csv("E:\VS codew\机器学习\实验三\Air_data.csv",header = 0)
print(data.shape)
print("1.载入数据，输出前五条")
print(data.head())

k = 5
kmodel = KMeans(max_iter=300,n_clusters=5,random_state=None,tol=0.0001)
kmodel.fit(data)

r1 = pd.Series(kmodel.labels_).value_counts() 
print('统计各个类别的数目')
print(r1)
r2 = pd.DataFrame(kmodel.cluster_centers_)#找出聚类中心
print('聚类中心:')
print(r2)
r = pd.concat([r2, r1], axis = 1)#聚类中心对应的类别下的数目
r.columns = list(data.columns) + [u'聚类个数']
print('查看聚类个数及中心点统计')
print(r)


plt.xlabel("ZL-ZR-ZF-ZM-ZC")
plt.ylabel("Custer-center-value")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.title("")
clu = kmodel.cluster_centers_ 
colors = ['red','green','yellow','blue','black']
x = [1,2,3,4,5]
for i in range(len(clu)):
    plt.plot(x,clu[i],label = u'cluster'+str(i),color=colors[i],marker='o')
plt.legend()
plt.show()


