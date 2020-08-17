import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

housings = pd.read_csv("housing2.csv",low_memory=False)
MEDV2 = housings['MEDV1'][1:]#把除第一天的数据重新保存在另一个列表
MEDV2.index = range (0,len(MEDV2))#重建索引并合并数据
housings['MEDV2'] = MEDV2#构建一个MEDV2的列索引
housings = housings.iloc[:-1,:]#去除最后一行
print(housings)

regressor = LinearRegression()
#predictor，变量需要一个dataframe而不能是一个series
predictors = housings[['MEDV1']]
to_predictors = housings ['MEDV2']
print(predictors)
print(to_predictors)
regressor.fit(predictors,to_predictors)
#根据模型生产预测值
MEDV2_predictor = regressor.predict(predictors)
print(MEDV2_predictor)