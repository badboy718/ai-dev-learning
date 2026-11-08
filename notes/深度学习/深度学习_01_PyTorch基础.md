[TOC]

# 深度学习_01_PyTorch基础

## 一、深度学习简介

### 1.1 概念

深度学习是机器学习的一类算法

以人工神经网络为结构，自动提取特征

### 1.2 特点

自动提取特征

解释性差

大量数据和高性能算力

非线性转换

### 1.3 常见模型

ANN 人工神经网络 感知机

CNN 卷积神经网络 图像、视频

RNN 循环神经网络 NLP

transformer RNN衍生

自编学习器

### 1.4 应用场景

自然语言处理 NLP

​	生成时AI AIGC LLM

​	机器翻译

​	语音识别

计算机视觉 CV

​	图像识别

​	面部解锁

​	视频合成

推荐系统

​	电影、音乐、文章、商品

---

## 二、PyTorch框架

pytorch是深度学习的框架、python三方包、数据以张量类型存在

特点：

​	张量数据类型

​	自动微分模块、自动求导/梯度

​	可以在GPU TPU NPU上加速运行

​	兼容各平台

---

## 三、张量创建

### 3.1 张量

​	矩阵，多维

​	0维度 -> 标量

​	1维度 -> [1,2,3,4]

​	2维度 -> [[1,2],[3,4]]

​	3维度 -> [[[1,1],

​			  [2,2]],

​			 [[3,3],

​			 [4,4]]]

### 3.2 基本创建方式

**补充：** `torch.tensor()` 会自动推断数据类型：列表浮点数→`float32`，整数→`int64`，Numpy数组保留原类型。

torch.tensor(data = )  指定数据

torch.Tensor(data = ,size = ) 指定数据以及形状

torch.IntTensor(data = )

torch.FloatTensor(data = )  指定数据类型

```python
import numpy as np
import torch

list1 = [[1.,2.,3.],[4,5,6]]
int1 = 10
n1 = np.array([[1.,2.,3.],[4.,5.,6.]])

t1 = torch.tensor(data = list1)
t2 = torch.tensor(data = int1)
t3 = torch.tensor(data = n1)

print(t1) 
#tensor([[1., 2., 3.],[4., 5., 6.]])
print(t1.dtype)  
#torch.float32
print(t2) 
#tensor(10)
print(t2.dtype) 
#torch.int64
print(t3) 
#tensor([[1., 2., 3.],[4., 5., 6.]], dtype=torch.float64)
print(t3.dtype) 
#torch.float64
```

### 3.3 线性张量和随机张量

**补充：** `manual_seed` 设置随机种子保证每次运行结果一致，方便调试。

​	线性张量

​		torch.arange(start = ,end = ,step = )  创建指定步长的线性张量 左闭右开

​		torch.linspace(start = ,end = ,steps = ) 创建指定元素个数的线性张量 左闭右闭

```python
import torch

t1 = torch.arange(start=0,end=10,step=2)
t2 = torch.linspace(start=0,end=10,steps=5)

print(t1) 
#tensor([0, 2, 4, 6, 8])
print(t2) 
#tensor([ 0.0000,  2.5000,  5.0000,  7.5000, 10.0000])

```

​	随机张量

​		torch.rand(size = ) / torch.randn(size = ) 创建指定形状的随机浮点类型张量

​		torch.randint(low = ,high = ,size = )  左闭右开 创建**指定形状**和**指定范围内随机整数**张量

​		torch.initial_seed()  查看随机种子

​		torch manual_seed(seed = )  设置随机种子

```python
import torch

torch.manual_seed(11)

t1 = torch.rand(2,3)
t2 = torch.randn(2,3)
t3 = torch.randint(low=0, high=5,size=(2,3))

print(torch.initial_seed()) #11

print(t1) 
#tensor([[0.1490, 0.4866, 0.9857],[0.1684, 0.5839, 0.6936]])
print(t2) 
#tensor([[-0.6700, -1.1277,  0.3497],[ 0.5125,  1.2068,  1.4048]])
print(t3) 
#tensor([[3, 1, 3],[2, 3, 4]])
```

### 3.4 零、一、指定值 张量

​	torch.zeros(size = )   torch.ones(size = )   torch.full(size = ,fill_value = )

根据形状创建全0张量，根据形状创建全1张量，根据形状创建全指定值张量

​	torch.zeros_like(input = )  torch.ones_like(input = )  torch.full_like(input = ,fill_value = )

根据指定张量的形状创建全0张量，根据指定张量的形状创建全1张量

根据指定张量的形状创建全指定值张量

```python
import torch

torch.manual_seed(11)

t1 = torch.rand(2,2)
print(t1)
# tensor([[0.1490, 0.4866],
#         [0.9857, 0.1684]])
print('*' * 30)、
#******************************

# 0
t0_1 = torch.zeros(2, 3)
t0_2 = torch.zeros_like(t1)
print(t0_1)
#tensor([[0., 0., 0.],
#        [0., 0., 0.]])
print(t0_2)
#tensor([[0., 0.],
#        [0., 0.]])

# 1
t1_1 = torch.ones(2, 3)
t1_2 = torch.ones_like(t1)
print(t1_1)
#tensor([[1., 1., 1.],
#        [1., 1., 1.]])
print(t1_2)
#tensor([[1., 1.],
#        [1., 1.]])

# 指定值
t2_1 = torch.full((2, 3), 5)
t2_2 = torch.full_like(t1, 5)
print(t2_1)
#tensor([[5, 5, 5],
#        [5, 5, 5]])
print(t2_2)
#tensor([[5., 5.],
#        [5., 5.]])
```

### 3.5 指定元素类型张量

tensor.type(dtype = )  dtype: 指定元素类型, 浮点类型默认是float32

tensor.half() / float() / double() / short() / int() / long()

```python
import torch

t1 = torch.tensor([[1, 2], [3, 4]],dtype=torch.float16)
print(t1.dtype)
#torch.float16
t2 = t1.type(dtype=torch.FloatTensor)
t3 = t1.type(dtype=torch.int64)
print(t2.dtype)
#torch.float32
print(t3.dtype)
#torch.int64

t4 = torch.tensor(data=[1,2])
print(t4.dtype)
#torch.int64
t5 = t4.int()
print(t5.dtype)
#torch.int32

```

---

## 四、张量类型转换

### 4.1 张量转换为Numpy数组

torch.numpy() 共享内存, 修改一个另外一个也跟着变, 可以通过copy()函数不共享内存

torch.numpy().copy()  

```python
import torch
import numpy as np

torch.manual_seed(112)

t1 = torch.randint(low = 0,high = 10,size = (2,3),dtype = torch.int32)
n1 = t1.numpy()
n1_copy = t1.numpy().copy()
print(t1,type(t1))
# tensor([[4, 3, 0],
#         [0, 3, 4]], dtype=torch.int32) <class 'torch.Tensor'>
print(n1,type(n1))
# [[4 3 0]
#  [0 3 4]] <class 'numpy.ndarray'>
print(n1_copy,type(n1_copy))
# [[4 3 0]
#  [0 3 4]] <class 'numpy.ndarray'>

n1[0][0] = 100
n1_copy[0][0] = 200
# n1 会影响 t1，而 .copy() 出来的 n1_copy 不影响原张量

print(t1,type(t1))
# tensor([[100,   3,   0],
#         [  0,   3,   4]], dtype=torch.int32) <class 'torch.Tensor'>
print(n1,type(n1))
# [[100   3   0]
#  [  0   3   4]] <class 'numpy.ndarray'>
print(n1_copy,type(n1_copy))
# [[200   3   0]
#  [  0   3   4]] <class 'numpy.ndarray'>

```

### 4.2 Numpy数组转换为张量

**本节新学：** `torch.from_numpy()` 共享内存，`torch.tensor()` 不共享内存，`torch.from_numpy(n1.copy())` 也不共享。

torch.from_numpy(ndarray = )

torch.tensor(data=n1)

```python
import torch
import numpy as np

n1 = np.array([[1, 2, 3],[4, 5, 6]])

# np转化张量
# 共享内存
t1 = torch.from_numpy(n1)

# 不共享内存
t2 = torch.tensor(data=n1)
t3 = torch.from_numpy(n1.copy())

print(n1,type(n1))
# [[1 2 3]
#  [4 5 6]] <class 'numpy.ndarray'>
print(t1,type(t1))
# tensor([[1, 2, 3],
#         [4, 5, 6]]) <class 'torch.Tensor'>
print(t2,type(t2))
# tensor([[1, 2, 3],
#         [4, 5, 6]]) <class 'torch.Tensor'>
print(t3,type(t3))
# tensor([[1, 2, 3],
#         [4, 5, 6]]) <class 'torch.Tensor'>
# 修改张量元素
t1[0][0] = 777
t2[0][0] = 888
t3[0][0] = 999
# 修改后
print(n1,type(n1))
# [[777   2   3]
#  [  4   5   6]] <class 'numpy.ndarray'>
print(t1,type(t1))
# tensor([[777,   2,   3],
#         [  4,   5,   6]]) <class 'torch.Tensor'>
print(t2,type(t2))
# tensor([[888,   2,   3],
#         [  4,   5,   6]]) <class 'torch.Tensor'>
print(t3,type(t3))
# tensor([[999,   2,   3],
#         [  4,   5,   6]]) <class 'torch.Tensor'>
```

### 4.3 提取标量张量的数值

tensor.item(): 提取单个元素张量的数值，**只对标量有效**（非标量会报错）

```python
import torch
import numpy as np

torch.manual_seed(112)
t1 = torch.tensor(data=[1])
#t1 = torch.randn(2,3) #报错
print(t1)
print(t1.item())
```

---

## 五、张量数值计算

### 5.1 基本运算

**补充：** 带下划线 `_` 的版本（如 `add_()`）是**原地操作**，直接修改原张量。

`+ ` `-` `*` `/` `-`

tensor/torch.add() sub() mul() div() neg()

`tensor/torch.add_()` `sub_()` `mul_()` `div_()` `neg_()`

```python
import torch

t1 = torch.tensor(data=[1,2,3,4])
print(t1)
# tensor([1, 2, 3, 4])
t2 = t1 + 10
print(t2)
# tensor([11, 12, 13, 14])
t3 = t1 + t2
print(t3)
# tensor([12, 14, 16, 18])

t4 = t1.add(other=100)
print(t4)
# tensor([101, 102, 103, 104])
t5 = torch.add(input=t1,other=200)
print(t5)
# tensor([201, 202, 203, 204])

t6 = t1.neg_()
print(t6)
# tensor([-1, -2, -3, -4])
```

### 5.2 点乘运算

  `*`  / mul() : 点乘：对应位置的元素进行点乘,，一般要求**两个张量形状相同** 

```python
import torch

t1 = torch.tensor(data = [[1,2],[3,4]])
t2 = torch.tensor(data = [[5,6],[7,8]])
t3 = t1 * t2
t4 = torch.mul(input=t1,other=t2)
print(t3)
# tensor([[ 5, 12],
#         [21, 32]])
print(t4)
# tensor([[ 5, 12],
#         [21, 32]])
```

### 5.3 矩阵乘法运算

`@`  / torch.matmul(input=, ohter=) ：矩阵乘法: (a.b) * (c,d) = (a, d)    **要求 b=c**  

第一个矩阵的行和第二个矩阵的列相乘  

```python
import torch

t1 = torch.tensor(data = [[1,2],[3,4]])
t2 = torch.tensor(data = [[5,6,7],[8,9,10]])
t3 = t1 @ t2
t4 = torch.matmul(input = t1,other = t2)
print(t3)
# tensor([[21, 24, 27],
#         [47, 54, 61]])
print(t4)
# tensor([[21, 24, 27],
#         [47, 54, 61]])
```

---

## 六、张量运算函数

**补充：** `dim` 参数指定沿哪个维度计算：`dim=0` 沿列、`dim=1` 沿行，计算后该维度消失。

torch.mean()：平均值

torch.sum()：求和

torch.sqrt()：开方、平方根

torch.pow(input = ,exponent = )：幂次方

torch.exp()：指数 e^x

torch.log()：对数 log() log2() log10()

```python
import torch

torch.manual_seed(113)

t1 = torch.tensor(data = [[1,2],[3,4],[5,6]], dtype=torch.float32)
t2 = torch.randn(size = (3,2,2))
print(t2)
# tensor([[[ 0.6245, -0.6969],
#          [ 1.0097, -2.1372]],
#
#         [[-0.9349,  0.0943],
#          [-0.1119,  0.5088]],
#
#         [[ 0.0861,  0.5399],
#          [ 1.6485, -0.8031]]])

# dim=d 就是把第 d 个坐标轴"拍扁"，输出 shape 里第 d 个数字消失

# mean() 平均值
print(t1.mean())
# tensor(3.5000)
print(t1.mean(dim=0))
# tensor([3., 4.])
print(t1.mean(dim=1))
# tensor([1.5000, 3.5000, 5.5000])
#print(t2.mean(dim=2))

# sum() 求和
print(t1.sum())
# tensor(21.)
print(t1.sum(dim=0))
# tensor([ 9., 12.])
print(t1.sum(dim=1))
# tensor([ 3.,  7., 11.])
#print(t2.sum(dim=2))

# sqrt 开方 全部值
print(t1.sqrt())
# tensor([[1.0000, 1.4142],
#         [1.7321, 2.0000],
#         [2.2361, 2.4495]])

# pow 幂次方
print(t1.pow(exponent=2))
# tensor([[ 1.,  4.],
#         [ 9., 16.],
#         [25., 36.]])

# exp() 指数 e^x
print(t1.exp())
# tensor([[  2.7183,   7.3891],
#         [ 20.0855,  54.5981],
#         [148.4132, 403.4288]])

# log() 对数
print(t1.log())
# tensor([[0.0000, 0.6931],
#         [1.0986, 1.3863],
#         [1.6094, 1.7918]])
print(t1.log2())
# tensor([[0.0000, 1.0000],
#         [1.5850, 2.0000],
#         [2.3219, 2.5850]])
print(t1.log10())
# tensor([[0.0000, 0.3010],
#         [0.4771, 0.6021],
#         [0.6990, 0.7782]])

```

---

## 七、张量索引

**本节新学：** 张量索引和Numpy类似，支持五种方式：简单行列索引、列表索引（取多个指定位置）、范围索引（切片）、布尔索引（条件筛选）、多维索引（3维以上张量）。

```python
import torch

torch.manual_seed(113)

data = torch.randint(0,10,[4,5])
print(data)
#tensor([[9, 4, 8, 6, 6],
#        [6, 6, 9, 9, 6],
#        [5, 8, 9, 8, 4],
#        [0, 9, 9, 5, 9]])

# 简单行、列索引
print(data[0])
# tensor([9, 4, 8, 6, 6])
print(data[:,0])
# tensor([9, 6, 5, 0])
print(data[0,0])
# tensor(9)
print(data[0:2,0:2])
# tensor([[9, 4],
#         [6, 6]])

# 列表索引
# 返回（0，1）、（1，2）两个位置的元素
print(data[[0,1],[1,2]])
# tensor([4, 9])
# 返回 0、1 行的 1 、2 列共4个元素
print(data[[[0],[1]],[1,2]])
# tensor([[4, 8],
#         [6, 9]])

# 范围索引
# 前3行的前2列数据
print(data[:3,:2])
# tensor([[9, 4],
#         [6, 6],
#         [5, 8]])
# 第2行到最后前2列数据
print(data[2:,:2])
# tensor([[5, 8],
#         [0, 9]])

# 布尔索引
# 第三列大于5的行数据
print(data[data[:,2] > 5])
# tensor([[9, 4, 8, 6, 6],
#         [6, 6, 9, 9, 6],
#         [5, 8, 9, 8, 4],
#         [0, 9, 9, 5, 9]])
# 第二行大于5的列数据
print(data[:,data[1] > 5])
# tensor([[9, 4, 8, 6, 6],
#         [6, 6, 9, 9, 6],
#         [5, 8, 9, 8, 4],
#         [0, 9, 9, 5, 9]])

# 多维索引
data = torch.randint(0,10,(3,4,5))
print(data)
# tensor([[[2, 1, 9, 5, 4],
#          [9, 0, 5, 1, 1],
#          [9, 6, 7, 9, 9],
#          [4, 7, 6, 9, 3]],
#
#         [[7, 4, 7, 7, 1],
#          [3, 2, 5, 6, 5],
#          [7, 3, 3, 7, 2],
#          [9, 7, 3, 7, 9]],
#
#         [[9, 3, 3, 2, 7],
#          [9, 4, 2, 8, 8],
#          [9, 5, 3, 0, 7],
#          [9, 1, 2, 5, 7]]])
# 获取0轴上的第一个数据
print(data[0,:,:])
# tensor([[2, 1, 9, 5, 4],
#         [9, 0, 5, 1, 1],
#         [9, 6, 7, 9, 9],
#         [4, 7, 6, 9, 3]])
# 获取1轴上的第一个数据
print(data[:,0,:])
# tensor([[2, 1, 9, 5, 4],
#         [7, 4, 7, 7, 1],
#         [9, 3, 3, 2, 7]])
```

---

## 八、张量形状

### 8.1 reshape

**本节新学：** `shape`/`size()` 查看形状；`reshape()` 改变形状（元素总数必须不变）。

```python
import torch

data = torch.randint(0,10,(2,3))
print(data)
# tensor([[9, 4, 6],
#         [0, 5, 7]])

# shape 或 size 都可以获得张量的形状
print(data.shape,data.shape[0])
# torch.Size([2, 3]) 2
print(data.size(),data.size(1))
# torch.Size([2, 3]) 3

# reshape 可以改变张量的形状
new_data = data.reshape(1,6)
print(new_data)
# tensor([[9, 4, 6, 0, 5, 7]])
```

### 8.2 squeeze unsqueeze

**本节新学：** `unsqueeze(dim)` 在指定位置**增加**维度为1的轴；`squeeze()` **去掉**所有维度为1的轴。

```python
import torch

data = torch.randint(0,10,(1,5))
print(data,data.shape)
# tensor([[6, 4, 2, 3, 5]]) torch.Size([1, 5])

data2 = data.unsqueeze(dim = 0)
print(data,data2.shape)
# tensor([[6, 4, 2, 3, 5]]) torch.Size([1, 1, 5])

data3 = data.unsqueeze(dim = 1)
print(data,data3.shape)
# tensor([[6, 4, 2, 3, 5]]) torch.Size([1, 1, 5])

data4 = data.unsqueeze(dim = -1)
print(data,data4.shape)
# tensor([[6, 4, 2, 3, 5]]) torch.Size([1, 5, 1])

data5 = data4.squeeze()
print(data5,data5.shape)
# tensor([6, 4, 2, 3, 5]) torch.Size([5])
```

### 8.3 transpose permute

**本节新学：** `transpose(dim1, dim2)` 交换两个轴；`permute([...])` 一次性重排所有轴的顺序。

```python
import torch

torch.manual_seed(114)
data = torch.randint(0,10,(3,4,5))
print(data)
# tensor([[[6, 9, 0, 6, 7],
#          [9, 2, 4, 4, 7],
#          [2, 1, 3, 4, 0],
#          [6, 5, 2, 0, 2]],
#
#         [[6, 7, 7, 3, 4],
#          [4, 0, 7, 9, 4],
#          [8, 1, 7, 5, 3],
#          [2, 0, 6, 6, 2]],
#
#         [[6, 2, 7, 5, 0],
#          [6, 2, 3, 3, 0],
#          [1, 0, 1, 1, 1],
#          [0, 8, 5, 5, 5]]])
data2 = torch.transpose(data,1,2)
print(data2.shape)
# torch.Size([3, 5, 4])
data3 = torch.transpose(data,0,1)
print(data3.shape)
# torch.Size([4, 3, 5])
data4 = torch.transpose(data3,1,2)
print(data4.shape)
# torch.Size([4, 5, 3])

# permute 函数将形状修改
data5 = torch.permute(data,[1,2,0])
print(data5.shape)
# torch.Size([4, 5, 3])
data6 = data.permute([1,2,0])
print(data6.shape)
# torch.Size([4, 5, 3])
```

### 8.4 view contiguous

**本节新学：** `view()` 改变形状但要求张量内存**连续**；`transpose` 等操作后可能不连续，需先 `.contiguous()` 再 `view`。

```python
import torch
torch.manual_seed(114)
data = torch.randint(0,100,(2,3))
print(data)
# tensor([[46, 99, 50],
#         [ 6,  7, 79]])
# 判断张量是否连续
print(data.is_contiguous())
# True
# view
data2 = data.view(3,2)
print(data2.shape)
# torch.Size([3, 2])
# data2 是否连续
print(data2.is_contiguous())
# True
# 使用transpose函数修改形状
data3 = torch.transpose(data,0,1)
print(data3.shape)
# torch.Size([3, 2])
# data3 是否连续
print(data3.is_contiguous())
# False
# 先使用contiguous()函数转换为连续的张量，再使用view
data4 = data3.contiguous().view(3,2)
print(data4.shape)
# torch.Size([3, 2])
# data4 是否连续
print(data4.is_contiguous())
# True
```

---

## 九、张量拼接

### 9.1 cat

cat()：沿着现有维度连接一系列张量。所有输入张量除了指定的拼接维度外，其他维度必须匹配。

```python
import torch
from numpy.ma.core import shape

torch.manual_seed(114)
data1 = torch.randint(0,100,(1,2,3))
data2 = torch.randint(0,100,(1,2,3))
print(data1,data1.shape)
# tensor([[[46, 99, 50],
#          [ 6,  7, 79]]]) torch.Size([1, 2, 3])
print(data2,data2.shape)
# tensor([[[52, 94, 44],
#          [97,  2, 91]]]) torch.Size([1, 2, 3])

# 1 按0维 拼接
new_data0 = torch.cat([data1,data2],dim=0)
print(new_data0,new_data0.shape)
# tensor([[[46, 99, 50],
#          [ 6,  7, 79]],
#
#         [[52, 94, 44],
#          [97,  2, 91]]]) torch.Size([2, 2, 3])
# 2 按1维 拼接
new_data1 = torch.cat([data1,data2],dim=1)
print(new_data1,new_data1.shape)
# tensor([[[46, 99, 50],
#          [ 6,  7, 79],
#          [52, 94, 44],
#          [97,  2, 91]]]) torch.Size([1, 4, 3])
# 3 按2维 拼接
new_data2 = torch.cat([data1,data2],dim=2)
print(new_data2,new_data2.shape)
# tensor([[[46, 99, 50, 52, 94, 44],
#          [ 6,  7, 79, 97,  2, 91]]]) torch.Size([1, 2, 6])

```

### 9.2 stack

stack()：在一个新的维度上连接一系列张量，这会增加一个新维度，并且所有输入张量的形状必须完全相同

```python
import torch

torch.manual_seed(114)
data1 = torch.randint(0,10,(2,3))
data2 = torch.randint(0,10,(2,3))
print(data1,data1.shape)
# tensor([[6, 9, 0],
#         [6, 7, 9]]) torch.Size([2, 3])
print(data2,data2.shape)
# tensor([[2, 4, 4],
#         [7, 2, 1]]) torch.Size([2, 3])

# 1 按0维 拼接
new_data0 = torch.stack([data1,data2],dim=0)
print(new_data0,new_data0.shape)
# tensor([[[6, 9, 0],
#          [6, 7, 9]],
#
#         [[2, 4, 4],
#          [7, 2, 1]]]) torch.Size([2, 2, 3])
# 2 按1维 拼接
new_data1 = torch.stack([data1,data2],dim=1)
print(new_data1,new_data1.shape)
# tensor([[[6, 9, 0],
#          [2, 4, 4]],
#
#         [[6, 7, 9],
#          [7, 2, 1]]]) torch.Size([2, 2, 3])
# 3 按2维 拼接
new_data2 = torch.stack([data1,data2],dim=2)
print(new_data2,new_data2.shape)
# tensor([[[6, 2],
#          [9, 4],
#          [0, 4]],
#
#         [[6, 7],
#          [7, 2],
#          [9, 1]]]) torch.Size([2, 3, 2])
```

---

## 十、自动微分模块

### 10.1 梯度计算

**本节新学：** `requires_grad=True` 开启自动微分；`.backward()` 反向传播计算梯度（要求标量，所以用 `loss.sum().backward()`）；梯度存在 `.grad` 中。

```python
import torch
# 创建标量张量 w权重
# requires_grad=True 是否自动微分
# dtype，自动微分的张量元素必须是浮点类型
w = torch.tensor(data = [10,20],requires_grad=True,dtype=torch.float32)
# 定义损失函数 计算损失值
loss = 2 * w ** 2
print(loss)
# tensor([200., 800.], grad_fn=<MulBackward0>)
print(loss.sum())
# tensor(1000., grad_fn=<SumBackward0>)
# 计算梯度，反向传播，loss 必须是标量张量 否则无法计算梯度
loss.sum().backward()
# 获取w
print(w.grad)
# tensor([40., 80.])
print(w)
# tensor([10., 20.], requires_grad=True)

```

### 10.2 梯度下降求最优解

**本节新学：** 手动实现梯度下降循环：梯度清零 → 反向传播 → 用 `w.data = w.data - 学习率 * w.grad` 更新参数。

```python
import torch

# 创建自动微分 w权重
w = torch.tensor(data=10,requires_grad=True,dtype=torch.float32)
print(w)
# 定义损失函数
loss = w**2 + 20
print(loss)
# 0.01 --> 学习率
print(f'开始 权重w初始值:{w} (0.01 * w.grad):无 损失值loss:{loss}')
for i in range(1,1001):
    loss = w ** 2 + 20
    # 梯度清零
    if w.grad is not None:
        w.grad.zero_()
    # 反向传播
    loss.sum().backward()
    # 梯度更新
    w.data = w.data - 0.01 * w.grad
    print(f'i 次数：{i} ')
    print(f'权重w: {w} ')
    print(f'0.01 * w.grad: {0.01 * w.grad} ')
    print(f'损失值loss: {loss} ')
print(f'w {w.grad},loss最小值 {loss}')
```

### 10.3 梯度计算注意点

**本节新学：** `detach()` 剥离张量得到新张量（不能自动微分，但与原张量共享数据）；`id()` 验证是否共享内存。

```python
import torch

x1 = torch.tensor(data=10,requires_grad=True,dtype=torch.float32)
print(x1)
# 判断张量是否自动微分，返回True/False
print(x1.requires_grad)
# 调用detach()方法对x1进行剥离，得到新的张量，不能自动微分，数据和原张量共享
x2 = x1.detach()
print(x2.requires_grad)
print(x1.data)
print(x2.data)
print(id(x1.data))
print(id(x2.data))
n1 = x2.numpy()
print(n1)
```

### 10.4 自动微分模块应用

**本节新学：** 完整训练流程：定义样本 → 初始化权重偏置 → 前向传播 → 计算损失 → 反向传播得梯度。这是所有神经网络训练的基础模式。

```python
import torch
from torch import nn
# todo:1 定义样本的 x 和 y
x = torch.ones(size=(2,5))
y = torch.zeros(size=(2,3))
print(x)
# tensor([[1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.]])
print(y)
# tensor([[0., 0., 0.],
#         [0., 0., 0.]])
# todo:2 初始模型权重 w b 自动微分张量
w = torch.randn(size=(5,3),requires_grad=True)
b = torch.randn(size=(3,),requires_grad=True)
print(w)
# tensor([[-0.2540, -0.5233,  1.1927],
#         [ 1.1908, -0.5981, -1.5200],
#         [ 0.8496,  0.8979,  0.0805],
#         [-1.0359,  0.9944,  1.1615],
#         [-0.6815,  1.0632,  0.0510]], requires_grad=True)
print(b)
# tensor([-0.1685, -0.2299,  0.3424], requires_grad=True)
# todo:3 初始模型，计算预测y值
y_pred = torch.matmul(x,w) + b
print(y_pred)
# tensor([[-0.0995,  1.6042,  1.3082],
#         [-0.0995,  1.6042,  1.3082]], grad_fn=<AddBackward0>)
# todo:4 根据MSE损失函数计算损失值
# 创建MSE对象，类创建对象
criterion = nn.MSELoss()
loss = criterion(y_pred,y)
print(loss)
# tensor(1.4316, grad_fn=<MseLossBackward0>)
# todo:5 反向传播，计算 w 和 b 梯度
loss.sum().backward()
print(w.grad)
# tensor([[-0.0663,  1.0695,  0.8721],
#         [-0.0663,  1.0695,  0.8721],
#         [-0.0663,  1.0695,  0.8721],
#         [-0.0663,  1.0695,  0.8721],
#         [-0.0663,  1.0695,  0.8721]])
print(b.grad)
# tensor([-0.0663,  1.0695,  0.8721])
```

---

## 十一、PyTorch构建线性回归模型

**补充：** 训练循环五步：`model(x)` 前向传播 → `criterion()` 计算损失 → `optimizer.zero_grad()` 梯度清零 → `loss.backward()` 反向传播 → `optimizer.step()` 更新参数。

1.准备训练集数据

2.构建要使用的模型

3.设置损失函数和优化器

4.模型训练

使用的api

- 使用 PyTorch 的 nn.MSELoss() 代替平方损失函数
- 使用 PyTorch 的 data.DataLoader 代替数据加载器
- 使用 PyTorch 的 optim.SGD 代替优化器
- 使用 PyTorch 的 nn.Linear 代替假设函数

```python
import torch
from torch.utils.data import TensorDataset   # 构造数据集对象
from torch.utils.data import DataLoader      # 数据加载器
from torch import nn                         # nn模块 平方损失函数 假设函数
from torch import optim                      # optim模块 优化器函数
from sklearn.datasets import make_regression # 创建线性回归模型数据集
import matplotlib.pyplot as plt              # plt 绘图
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False   # 用来正常显示负号

# todo:1 构建线性回归 数据集
def create_dataset():
    # 1： 创建数据集
    # 采用make_regression() 创建回归数据集
    x,y,coef = make_regression(
        n_samples=100,   # 样本数量
        n_features=1,    # 特征数量
        n_targets=1,     # 目标数量
        bias=15,         # (初始)偏置
        noise=10,        # 噪声
        coef=True,       # 返回系数
        random_state=116 # 随机种子
    )

    # 2 把上述 x（特征），y（标签） 封装成张量
    # 进化路线：
    # 数据 --> Tensor张量 --> TensorDataset数据集对象 --> Dataloader数据加载器
    x = torch.tensor(x,dtype=torch.float32)
    y = torch.tensor(y,dtype=torch.float32)

    # 3 返回结果
    print(f'x:{x.shape}, y:{y.shape}, coef:{coef}')
    print(f"x:{x}")
    print(f"y:{y}")
    print(f'coef:{coef}')

    return x,y,coef

# todo:2 模型训练
def train(x,y,coef):
    # 1.基于x,y构建数据集对象
    # 流程：数据 --> Tensor张量 --> TensorDataset数据集对象 --> DataLoader数据加载器
    dataset = TensorDataset(x, y)
    # 2.基于上述的 张量数据集 构建数据加载器
    dataloader = DataLoader(
        dataset,            # 数据集对象
        batch_size=15,      # 批处理数量（100/15  6个15样本，一个10样本，共7批）
        shuffle=True        # 是否打乱数据 （tips: 训练集打乱，测试集不打乱）
    )
    # 3.构建（线性回归）模型
    model = nn.Linear(
        in_features=1,    # 输入特征数量
        out_features=1    # 输出标签数量
    )
    # 4.构建损失函数 -> MSE（均方误差）
    criterion = nn.MSELoss()
    # 5.构建优化器 这里是模拟：随机梯度下降
    optimizer = optim.SGD(
        model.parameters(), # 待优化的模型参数
        lr = 0.01           # 优化器的学习率
    )
    # 6.模型训练
    # 6.1 定义变量，记录：训练的总轮数，每轮的平均损失，总损失，训练的样本数
    epochs,loss_list,total_loss,train_samples = 100,[],0.0,0
    # 6.2 具体的每轮训练的过程
    for epoch in range(epochs):
        # ------------------  完整的 一轮 训练 从这开始 --------------------------------------

        # 6.3 每轮都会针对于100条数据，按15条/批 进行训练，这是具体每批次的训练过程
        for train_x,train_y in dataloader:
            #-------------------------- 完整的 一批次 训练 从这开始 ---------------------------
            # 6.4 模型预测（前向传播，正向传播）
            y_pred = model(train_x)
            # 6.5 计算损失，细节：把真实值转成 n行1列的维度，方便和预测值计算
            loss = criterion(y_pred,train_y.reshape(-1,1))  # loss是该批次的平均损失，例如：15条数据的平均损失
            # 6.6 计算总损失
            total_loss += loss.item()
            # 6.7 计算训练的样本数（批次数）
            train_samples += 1
            # 6.8 梯度清零 反向传播（计算梯度），更新参数
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()     # 等价于 w新 = w旧 - 学习率 * 梯度
            # --------------------------完整的 一批次训练 到这结束 -------------------

        # 6.9 统计本轮的平均损失，并添加到列表中
        loss_list.append(total_loss / train_samples)
        # 6.10 输出训练信息
        print(f'轮数：{epoch + 1}, 平均损失：{total_loss / train_samples:.4f},训练样本数：{train_samples}')
        # ------------------完整的 一轮训练 到这结束 --------------------------------------

    # 6.11 打印最终信息
    print(f'训练完成，模型参数：{model.state_dict()}')

    # 7. 可视化.
    # 7.1 绘制损失变化曲线图.
    plt.plot(range(epochs), loss_list)
    plt.xlabel('训练的轮数')
    plt.ylabel('该轮的平均损失值')
    plt.title('损失变化曲线图')
    plt.grid()  # 网格
    plt.show()

    # 7.2 绘制拟合直线.
    # 7.2.1 绘制数据集(真实样本, 标签) 散点图
    plt.scatter(x, y)
    # 7.2.2 生成1000个x值(等差数列), 预测对应的y值.
    x = torch.linspace(x.min(), x.max(), 1000)

    # 7.2.3 计算预测值.
    y_pred = torch.tensor([v * model.weight + model.bias for v in x])  # model.weight: 21.2486, model.biasL: 14.6950
    # 7.2.4 计算真实值.
    y_true = torch.tensor([v * coef + 14.5 for v in x])  # (真实)权重:20.648364149092824, (真实)偏置:14.5

    # 7.2.5 绘制预测值 和 真实值的拟合回归线(直线)
    plt.plot(x, y_pred, label='预测值', color='red')
    plt.plot(x, y_true, label='真实值', color='green')

    # 7.2.6 绘制图例, 网格, 标题.
    plt.legend()
    plt.grid()
    plt.title('(PyTorch版)线性回归 -> 预测值和真实值关系')
    plt.show()


# todo n.测试代码
if __name__ == '__main__':
    x,y,coef = create_dataset()
    train(x,y,coef)

```
