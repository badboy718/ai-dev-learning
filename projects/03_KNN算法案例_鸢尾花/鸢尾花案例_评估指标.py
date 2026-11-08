from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score

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

# 6. 模型评估.
# 方式1: 直接评分, 基于: 测试集的特征 和 测试集的标签.
print(f'准确率: \n{estimator.score(x_test, y_test)}')  # 0.9666666666666667

# 方式2: 基于 测试集标签(真实值) 和 模型预测结果(预测值) 进行评分.
print(f'准确率: \n{accuracy_score(y_test, y_predict)}')  # 0.9666666666666667

# 测试模型评估指标: 精确率,召回率,f1值
# 参1: 真实值, 参2: 预测值, 参3: average表示 计算方式, 默认是macro(意思是 宏平均, 就是把所有分类都计算出来, 然后求平均).
print(f'精确率: \n{precision_score(y_test, y_predict, average="macro")}')  # 0.9666666666666667
print(f'召回率: \n{recall_score(y_test, y_predict, average="macro")}')  # 0.9629629629629629
print(f'f1值: \n{f1_score(y_test, y_predict, average="macro")}')  # 0.9628482972136222
