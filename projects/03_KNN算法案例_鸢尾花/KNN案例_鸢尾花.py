"""
案例：
    通过KNN算法实现 鸢尾花 的分类操作

回顾：
    机器学习流程
    1.数据加载
    2，数据预处理
    3，特征工程
    4，模型训练
    5，模型评估
    6，模型预测
"""
from sklearn.datasets import load_iris
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# todo 1.定义函数，加载鸢尾花数据集并查看
def dm01_load_iris():
    # 1 加载鸢尾花数据集
    iris_data = load_iris()

    # 2 查看数据集
    #print(iris_data)
    #print(iris_data.data)
    #print(type(iris_data))
    print(iris_data.keys())

    # 3 查看具体数据集
    print(iris_data.data[:5])
    print(iris_data.target[:5])
    print(iris_data.target_names)
    print(iris_data.feature_names)

# todo 2.定义函数 绘制数据集的散点图
def dm02_show_iris():
    # 1 加载数据集
    iris_data = load_iris()
    # 2 把鸢尾花数据集封装成DataFrame对象
    iris_df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    # 3 给df对象新增一列 -> 标签列
    iris_df['label'] = iris_data.target

    # 4 通过Seaborn绘制散点图
    sns.lmplot(
        data=iris_df,          # data = 数据集(鸢尾花的df对象）
        x='sepal length (cm)', # x = x轴（这里是花萼的长（sepal length (cm)））
        y='sepal width (cm)',  # y = y轴（这里是花萼的宽）
        hue='label',           # 分组字段
        fit_reg=False          # 是否显示回归线 默认True
    )
    plt.title('iris data')
    plt.tight_layout()
    plt.show()

# todo 3.定义函数 实现鸢尾花：完整流程
def dm03_iris_evaluate_test():
    # 1 数据加载
    iris_data = load_iris()
    # 2 数据预处理
    x_train, x_test, y_train, y_test = train_test_split(
        iris_data.data, # 特征数据
        iris_data.target,      # 标签数据
        test_size=0.2,         # 测试集占比
        random_state=30        # 随机种子
    )
    # 3 特征工程
    # 3.1 创建标准化对象
    transfer = StandardScaler()
    # 3.2 对训练集的特征列 进行标准化处理
    x_train = transfer.fit_transform(x_train) # 训练 + 转换
    # 3.3 对测试集的特征列 进行标准化处理
    x_test = transfer.transform(x_test)
    # 4 模型训练
    # 4.1 创建KNN分类对象
    model = KNeighborsClassifier(n_neighbors=3)
    # 4.2 模型训练
    model.fit(x_train, y_train)
    # 5 模型预测
    # 场景 1 对刚才的测试集进行测试
    y_pred = model.predict(x_test)
    print(y_pred[:5])
    # 场景 2 对新的数据集测试 可理解为验证集
    new_data = [[7.8,2.1,3.9,1.6]]
    new_data = transfer.transform(new_data)
    y_pre_new = model.predict(new_data)
    print(y_pre_new)
    # 6 模型评估
    # 方式 1 直接评分 基于 测试集的特征 和 测试集的标签
    print(model.score(x_test, y_test))
    # 方式 2 基于 测试集标签（真实值） 和 模型预测结果（预测值）进行评分
    print(accuracy_score(y_test, y_pred))
if __name__ == '__main__':
    #dm01_load_iris()
    #dm02_show_iris()
    dm03_iris_evaluate_test()