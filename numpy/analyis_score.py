import numpy as np
import pandas as pd
f = open('C:\\Users\\李纯罡\\Desktop\\模板-发给学生\\物联18大一学年成绩2.csv','r')
all_score = pd.read_csv(f)
print(all_score)
english_scores = all_score['English Scores']
caculates_scores = all_score['Caculates scores']
linearalgebra_score = all_score['Linearalgebra score']
ec = np.corrcoef(english_scores,caculates_scores)
el = np.corrcoef(english_scores,linearalgebra_score)
cl = np.corrcoef(caculates_scores,linearalgebra_score)
print("英语与高数的相关性为")
print(ec)
print("英语与线性代数的相关性为")
print(el)
print("高数与线性代数的相关性为")
print(cl)
xjt = {}
xjt['英语成绩和高数成绩的相关性最高']=ec[0][1]
xjt['英语成绩和线性代数成绩的相关性最高']=el[0][1]
xjt['高数成绩和线性代数成绩的相关性最高']=cl[0][1]
print(max(xjt,key = xjt.get))