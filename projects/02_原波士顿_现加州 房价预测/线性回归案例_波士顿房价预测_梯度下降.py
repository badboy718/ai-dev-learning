'''
案例：
    线性回归对象 梯度下降 波士顿房价预测

知识点：
    监督学习（有特征、有标签、且连续）之线性回归算法
    线性回归分类：
        1元线性回归：一个特征列、一个标签列
            公式：y = wx + b
        多元线性回归：多个特征列、一个标签列
            公式：y = w1x1 + w2x2 + ... + wNxN + b
                   = w的转置 * x + b

问1: 如何衡量线性回归模型的好还?
    通过损失函数实现即可, 损失函数值越小, 模型的效果越好.
问2: 线性回归常用的 损失函数有:
    最小二乘: 每个样本点误差的平方和.
    MSE: 均方误差, 每个样本点误差的平方和 / 样本总数.
    RMSE: 均方根误差, 平方根(MSE)
    MAE: 平均绝对误差, 每个样本点误差的绝对值和 / 样本总数.
    细节:
        1.一般 RMSE要比MAE要大一点.
        2. RMSE会放大误差(因为有平方), 所以它对异常点更敏感.
问3: 如何计算损失函数的最小值?
    思路1: 正规方程法, 一步到位直接计算出 最优的w, b
    思路2: 梯度下降法, 迭代求解. 获取"最优"的w, b

流程：
1.加载数据
2.数据预处理
3.特征工程
4.模型训练
5.模型预测
6.模型评估
'''

#from sklearn.datasets import load_boston
# ↑波士顿数据 黑哥们人种歧视问题被OTA了
import pandas as pd
import numpy as np
# ↓加州数据
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.metrics import mean_squared_error, root_mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1.加载数据

#孩子们不要怕，还有URL
#又被举报了 陨落了
#换成加州数据了
#data_url = "http://lib.stat.cmu.edu/datasets/boston"
#raw_df = pd.read_csv(data_url, sep="\\s+", skiprows=22, header=None)
#data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
#target = raw_df.values[1::2, 2]

california_housing = fetch_california_housing()
data = california_housing.data
target = california_housing.target

#print('特征',data.shape)
#print('标签',target.shape)
#print('特征前五行',data[:5])
#print('标签前五行',target[:5])

# 2.数据预处理
# 参1: 特征数据, 参2: 标签数据,
# 参3: 测试集所占比例, 参4: 随机种子(如果种子一致, 每次获取的数据都是"固定"随机的)
x_train, x_test, y_train,y_test = train_test_split(
    data, target, test_size=0.2, random_state=42)
#print(x_train.shape)
#print(y_train.shape)
#print(x_test.shape)
#print(y_test.shape)

# 3.特征工程
# 3.1 创建 标准化对象
transfer = StandardScaler()
# 3.2 对训练集和测试集的 特征数据 进行标准化
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# 4.模型训练
# 4.1 创建 线性回归 正规方程 模型对象
estimator = SGDRegressor(
    fit_intercept=True,        # fit_intercept: 是否计算偏置
    learning_rate='constant',  #learning_rate: 学习率策略
    eta0=0.0001,                  #eta0: 学习率大小
    max_iter=10000,
    tol=1e-3
)
# 4.2 模型训练
estimator.fit(x_train, y_train)
# 4.3 看看 w 和 b
#print('w',estimator.coef_)
#print('b',estimator.intercept_)

# 5.模型预测
y_predict = estimator.predict(x_test)
print('预测结果',y_predict)
# 6.模型评估
print('MSE',mean_squared_error(y_test,y_predict))
print('RMSE',root_mean_squared_error(y_test,y_predict))
print('MAE',mean_absolute_error(y_test,y_predict))

#MSE 0.5636720385537163
#RMSE 0.7507809524446636
#MAE 0.5326008744122401
