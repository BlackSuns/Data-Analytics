import csv
f = open("2014.csv",'r',encoding='utf-8')
csvreader = csv.reader(f)
new = list (csvreader)
new = new [1:]

a_ben = []
b_ben = []
c_ben = []
int_math_score = []
int_art_score = []
for i in new:
    if i [3] == "本科一批" :
        a_ben.append(i[4])
    if i [3] == "本科二批" :
        b_ben.append(i[4])
    if i [3] == "本科三批" :
        c_ben.append(i[4])
print("本科一批" + str(a_ben))
print("本科二批" + str(b_ben))
print("本科三批" + str(c_ben))
w = a_ben
step = 2
wenli = [w[i:i + step]for i in range(0,len(w),step)]
for i in wenli:
    li = i[0]
    wen = i [1]
    int_math_score.append(li)
    int_art_score.append(wen)
print("理科")
print(int_math_score)
print("文科")
print(int_art_score)

li_max = 0
for maxs in int_math_score:
    if int(li_max) < int(maxs):
        li_max = maxs
print("理科最高分")
print(li_max)
wen_max = 0
for maxs1 in int_art_score:
    if int(wen_max) < int(maxs1):
        wen_max = maxs1
print("文科最高分")
print(wen_max)


