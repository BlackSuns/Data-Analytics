import pandas as pd
import matplotlib.pyplot as plt
import datetime
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
import random

#使图不会产生乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#by xujintao  https://github.com/BlackSuns/python
data = pd.read_csv("Amazon.csv")
#print(data)
print(data.info())
#data['Open'] = data['Open'].astype(float)

#1.试分析从1997-2020年间股票价格哪天最高
max_price = max(data['High'])
print(max_price)
judge = data ['High'] == max_price
date = data['Date'].loc[judge]
print(date)
#2.试分析从1997-2020年间股票的走势

b= data['Date'].apply(lambda x:datetime.strptime(x,'%Y/%m/%d'))
data['Date_2'] = b#在赋值时添加个copy(),确保两个值不相同,否则出现奇怪的错误
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#rot : int, default None#设置轴标签（轴刻度）的显示旋转度数
data.plot( x = 'Date_2',y = 'Close', rot=30, figsize=(15, 8), title='amazon股价')#设置图形的大小，a 为图形的宽， b 为图形的高，单位为英寸
plt.show()
#3.试分析2019年中四个季度的股票涨落情况
data['year'] = data['Date'].apply(lambda x: x[:4])
print(type(data['year'][1]))
data['year'] = data['year'].astype(int)
is_2019 = data ['year'] == 2019
slice_data = data.loc[is_2019]
#print(slice_data)


a = slice_data['Date'].apply(lambda x:datetime.strptime(x,'%Y/%m/%d'))
slice_data['Date'] = a#在赋值时添加个copy(),确保两个值不相同,否则出现奇怪的错误


#slice_data['quarter'] = slice_data['Date'].apply(lambda x:datetime.strptime(x,'%m'))
#slice_data['quarter'].strip().strip('/')
#slice_data['quarter'] = slice_data['Date'].apply(lambda x:x[5:7])
#slice_data['quarter'] = slice_data['quarter'].astype(int)
#print(slice_data)
slice_data.index = slice_data['Date']
slice_data['close-open'] = slice_data['Close'] - slice_data['Open']

#print(slice_data)
one_quarter = slice_data ['2019-01-01':'2019-03-31']
two_quarter = slice_data ['2019-04-01':'2019-06-30']
three_quarter = slice_data ['2019-07-01':'2019-09-30']
four_quarter = slice_data ['2019-10-01':'2019-12-31']
#print(one_quarter)

plt.figure(figsize=(20,10),dpi=108) # figsize设置图片大小，dpi设置清晰度
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.subplot(411)
plt.title('2019年第一季度股票涨跌幅度')
plt.plot(one_quarter['Date'],one_quarter['close-open'],'pink')
plt.subplot(412)
plt.title('2019年第二季度股票涨跌幅度')
plt.plot(two_quarter['Date'],two_quarter['close-open'],'g',)#title='2019年第二季度股票涨跌幅度'
plt.subplot(413)
plt.title('2019年第三季度股票涨跌幅度')
plt.plot(three_quarter['Date'],three_quarter['close-open'],'y')
plt.subplot(414)
plt.title('2019年第四季度股票涨跌幅度')
plt.plot(four_quarter['Date'],four_quarter['close-open'],'m')
plt.show()


#试分析股票价格与交易数量是否有关系
#plt.figure(figsize=(30,30),dpi=108) # figsize设置图片大小，dpi设置清晰度

data ['Mean'] = data[['High', 'Low']].mean(axis=1)
#print(data)
plt.title('股票最高价格与交易数量关系图')
plt.plot(data['High'],data['Volume'],'co')
plt.show()
plt.plot(data['Low'],data['Volume'],'ko',)
plt.show()
plt.plot(data['Close'],data['Volume'],'bo',)
plt.show()
plt.plot(data['Mean'],data['Volume'],'ro',)
plt.show()
print("价格与交易数量相关系数")
Mean = data['Mean']
Volume = data['Volume']
a = np.corrcoef(Mean,Volume)
print(a)
if a[0][1] < 0.5 :
    print("相关性低")
#print(data['Mean'].corrwith(['Volume']))

#5.试分析开盘价格和当天最高价最低价是否有关系
plt.title('开盘价格和当天最高价关系图')
plt.plot(data['Open'],data['High'],'co')
plt.show()
plt.title('开盘价格和当天最低价关系图')
plt.plot(data['Open'],data['Low'],'go')
plt.show()

#6.试分析能否根据已有的数据去预测股票价格

data_2 = data[1:]#去除第一天无用数据
MEDV2 = data_2['Adj Close']
MEDV2 = MEDV2.reset_index(drop=True)
#MEDV2.index = range (0,len(MEDV2))#重建索引并合并数据
data['Adj Close_2'] = MEDV2
data = data.iloc[:-1]#删除多余的最后一行
data['Adj Close'] = data['Adj Close'].astype(float)#转换数据为float类型
data['Adj Close_2'] = data['Adj Close_2'].astype(float)
#rint(housings['MEDV1'].dtype)#转换数据格式
#2
np.random.seed(1)#seed( ) 用于指定随机数生成时所用算法开始的整数值，如果使用相同的seed( )值，则每次生成的随即数都相同
random.seed(1)
#随机重排housing数据
data = data.loc[np.random.permutation(data.index)]
#对data数据进行随机重排之后将数据分为训练数据和测试数据，比例为7:3；
print(data.shape[0])
hight_train_row = int (data.shape[0]*.7)#shape函数的功能是读取矩阵的长度，比如shape[0]就是读取矩阵第一维度的长度,相当于行数。它的输入参数可以是一个整数表示维度，也可以是一个矩阵。
print(hight_train_row)
train = data.loc[:hight_train_row,:]
test = data.loc[hight_train_row:,:]
regressor = LinearRegression()
#predictor，变量需要一个dataframe而不能是一个series
predictors = train[['Adj Close']]
to_predictors = train ['Adj Close_2']
regressor.fit(predictors,to_predictors)
#根据模型生产预测值
MEDV2_predictor = regressor.predict(test[['Adj Close']])
print(MEDV2_predictor)
#均方差
mse = sum((MEDV2_predictor - test['Adj Close_2'])**2)/len(MEDV2_predictor)
print("均方差")
print(mse)
mae = sum(abs(MEDV2_predictor-test['Adj Close_2']))/len(predictors)
print("平均绝对误差")
print(mae)
plt.title( '预测结果折线图')
plt.scatter(data['Adj Close'],data['Adj Close_2'],color = 'r')
plt.plot(test['Adj Close'],MEDV2_predictor,'k')
plt.show()













'''
1.试分析从1997-2020年间股票价格哪天最高

2.试分析从1997-2020年间股票的走势

3.试分析某年中四个季度的股票涨落情况

4.试分析股票价格与交易数量是否有关系

5.试分析开盘价格和当天最高价最低价是否有关系

6.试分析能否根据已有的数据去预测股票价格
'''
