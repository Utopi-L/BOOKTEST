from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# 加载鸢尾花数据集
iris = load_iris()

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=0)

# 训练决策树模型
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_train, y_train)

# 测试模型
print("Test accuracy:", clf.score(X_test, y_test))
