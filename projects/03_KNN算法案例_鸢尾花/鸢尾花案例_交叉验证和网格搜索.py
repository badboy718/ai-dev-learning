from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


# 1 数据加载
iris = load_iris()

# 2 数据预处理
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)

# 3 特征工程
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# 4 模型训练
estimator = KNeighborsClassifier()

# 不同之处 交叉验证和网格搜索
# 4.2 定义字典，记录超参可能出现的值
param_dict = {"n_neighbors": [1,2,3,4,5,6,7,8,9,10]}
# 4.3 创建GridSearchCV对象
estimator = GridSearchCV(
    estimator,               # 计算的对象
    param_grid=param_dict,   # 超参可能出现的值
    cv=4)                    # 交叉验证的次数
estimator.fit(x_train, y_train)
# 4.3 打印最优的参数组合
print(f'最优评分: {estimator.best_score_}')             # 0.95
print(f'最优参数组合: {estimator.best_params_}')         # {'n_neighbors': 4}
print(f'最优的模型对象: {estimator.best_estimator_}')    # KNeighborsClassifier(n_neighbors=4)

# 5 模型预测
y_predict = estimator.predict(x_test)
print(f'预测结果: {y_predict}')

# 6 模型评估
# 方式 1 直接评分 基于 测试集的特征 和 测试集的标签
print(estimator.score(x_test, y_test))
# 方式 2 基于 测试集标签（真实值） 和 模型预测结果（预测值）进行评分
print(accuracy_score(y_test, y_predict))