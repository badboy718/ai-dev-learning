import pandas as pd

#列表创建一维数组Series
s1 = pd.Series([1,2,3,4,5,6])
print(s1)
#字典创建一维数组Series
s2 = pd.Series({'a':1,'b':2,'c':3,'d':4})
print(s2)

#指定索引
s3 = pd.Series([10,20,30],index=['x','y','z'])
print(s3)
print(s3.values)
print(s3.index)

#二维表格数据 Dataframe
#字典格式
data = {
    '姓名':['张三','李四','王五','赵六'],
    '年龄':[25,30,35,28],
    '城市':['北京','上海','广州','深圳'],
    '工资':[5000,7000,6000,8000]
}
df = pd.DataFrame(data)
print(df)
#列表格式
data_list = [
    ['张三',25,'北京',5000],
    ['李四',30,'上海',7000],
    ['王五',35,'广州',6000],
    ['赵六',28,'深圳',8000]
]
df2 = pd.DataFrame(data_list)
print(df2)
#查看属性
print('形状',df2.shape)
print('列名',df.columns)
print('索引',df.index)