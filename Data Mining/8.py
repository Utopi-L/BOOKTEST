import numpy as np
from sklearn.datasets import load_iris

def sigmoid(A):
    return 1 / (1 + np.exp(-A))

def costfunc(h,y,m,thetaVec,Lambda): # 代价函数  h：估计函数结果  y：目标  m：样本数
    theta1=thetaVec[0]
    theta2=thetaVec[1]
    theta3=thetaVec[2]
    theta = np.sum(theta1[:,1:]**2) + np.sum(theta2[:,1:]**2) + np.sum(theta3[:,1:]**2)
    return -1/m*np.sum(y*np.log(h)+(1-y)*np.log(1-h)) + Lambda / (2 * m) * theta

def change(theta): #去掉第0列
    theta[:, 0] = 0
    return theta

def forward(X,thetaVec):
    a2=sigmoid(thetaVec[0] @ X)
    a2=np.insert(a2, 0, values=[1], axis=0)
    a3=sigmoid(thetaVec[1] @ a2)
    a3=np.insert(a3, 0, values=[1], axis=0)
    a4=sigmoid(thetaVec[2] @ a3)
    return a2,a3,a4

#导入训练集、测试集
iris_dataset = load_iris()
X=np.array(iris_dataset['data'])
X=np.insert(X, 0, values=[1], axis=1)
X_test=X[4::5].T
X_train=np.concatenate([X[0::5],X[1::5],X[2::5],X[3::5]]).T

y_temp=np.array(iris_dataset['target'])
y=np.zeros((3,150))
for i in range(0,150):
    if y_temp[i]==0:
        y[0,i]=1 #[1,0,0]
    elif y_temp[i]==1:
        y[1,i]=1 #[0,1,0]
    else:
        y[2,i]=1 #[0,0,1]
y_test=np.array(y[:,0::5])
y_train=np.concatenate([y[:,1::5],y[:,2::5],y[:,3::5],y[:,4::5]],axis=1)

m=120
Lambda=0 #正则化系数
learning_rate=0.02
flag=0

#输入：4个单元 隐藏层：2层 每层4个单元 输出层：3个单元
theta1=-1+2*np.random.random((4,5))
theta2=-1+2*np.random.random((4,5))
theta3=-1+2*np.random.random((3,5))
Delta4=np.zeros((3,m))
Delta3=np.zeros((5,m))
Delta2=np.zeros((5,m))

while True:#梯度下降
    #正向传播
    thetaVec=(theta1,theta2,theta3)
    a2_train,a3_train,a4_train=forward(X_train,thetaVec)

    J=costfunc(a4_train,y_train,m,thetaVec,Lambda)
    print('J=',J)
    if J<0.15:break

    #逆向传播
    Delta4=a4_train - y_train
    Delta3=theta3.T @ Delta4 * (a3_train * (1-a3_train))
    Delta3=np.delete(Delta3,0,axis=0)
    Delta2=theta2.T @ Delta3 * (a2_train * (1-a2_train))
    Delta2=np.delete(Delta2,0,axis=0)

    theta1_temp = change(theta1)
    theta2_temp = change(theta2)
    theta3_temp = change(theta3)
    D3=Delta4 @ a3_train.T / m + Lambda * theta3_temp
    D2=Delta3 @ a2_train.T / m + Lambda * theta2_temp
    D1=Delta2 @ X_train.T / m + Lambda * theta1_temp

    theta3-=learning_rate*D3
    theta2-=learning_rate*D2
    theta1-=learning_rate*D1

    if flag<1:
        flag+=1
    elif flag==1: #梯度检测 检查D是否正确
        thetaVec2=[theta1,theta2,theta3]
        DVec=(D1,D2,D3)
        grad_test=[0,0,0]
        for i in range(0,3):
            thetaVec2[i]+=0.00001
            a2_temp,a3_temp,a4_temp=forward(X_train,thetaVec2)
            grad_plus=costfunc(a4_temp,y_train,m,thetaVec2,Lambda)
            thetaVec2[i]-=0.00002
            a2_temp,a3_temp,a4_temp=forward(X_train,thetaVec2)
            grad_minus=costfunc(a4_temp,y_train,m,thetaVec2,Lambda)
            grad=(grad_plus-grad_minus)/(2*0.00001)
            grad_test[i]=grad-np.sum(DVec[i])
            thetaVec2[i]+=0.00001
        flag+=1

print('梯度检测：',grad_test)

#测试
a2_test, a3_test, a4_test = forward(X_test, thetaVec)
a4_test=np.rint(a4_test)

s=0
for i in range(0,30):
    if a4_test[0,i]==y_test[0,i] and a4_test[1,i]==y_test[1,i]:
        s+=1
print('测试得分：',s/30)

#使用模型
new=[[1],[5],[2.9],[1],[0.2]]
a2_new, a3_new, a4_new = forward(new, thetaVec)
print(np.rint(a4_new))