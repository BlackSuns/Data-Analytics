import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats
data = pd.read_csv('housing2.csv',low_memory=False)
#增加新的一列 MEDV2
MEDV2 = data['MEDV1'][1:]
MEDV2.index = range (0,len(MEDV2))
data['MEDV2'] = MEDV2
data = data.iloc[:-1,:]
#data
print(data)

data = data.loc[np.random.permutation(data.index)]#进行数据data随机重拍
#data
#选择前70%的数据作为训练数据
highest_train_row = int (data.shape[0]*.7)
train = data.loc[:highest_train_row,:]
#选择后30%的数据作为测试数据
test = data.loc[highest_train_row,:]
data['MEDV1'] = data['MEDV1'].astype(float)
data['MEDV2'] = data['MEDV2'].astype(float)
regressor = LinearRegression()
#predictors变量需要一个dataframe,而不能是一个series
predictors = data[['MEDV1']] #这是一个dataframe
to_predict = data ['MEDV2'] #这是一个series
print(predictors)
print(to_predict)
#训练线性回归模型
regressor.fit(predictors,to_predict)
#根据模型生成预测值
MEDV2_predictor = regressor.predict(predictors)
print(MEDV2_predictor)
x = np.array(data['MEDV1'])
y = np.array(data['MEDV2'])
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
print('slope:',slope) # float,斜率
print('intercept:',intercept) # float,截距
print('r_value:',r_value) #相关系数
print('p_value:',p_value) #假设检验的中斜率为 0 时的双侧 P 值
print('slope_std_error:',slope_std_error) #梯度估计的标准差
plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope*x, 'r', label='fitted line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('The relationship between x and y')
plt.legend()
plt.show()
predict_y = intercept + slope * x
pred_error = y - predict_y
degrees_of_freedom = len(x) - 2
print("MAE:",np.sum(pred_error) / degrees_of_freedom)
print("MSE:",np.sum(pred_error**2) / degrees_of_freedom )
#生成预测值与真实房价的散点图
plt.scatter(data['MEDV1'],data['MEDV2'])
plt.plot(data['MEDV1'],MEDV2_predictor)
plt.show()
