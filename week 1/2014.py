
f = open("2014.csv","r",encoding='utf-8')
data = f.read()
rows = data.split("\n")
print(rows)
rows = rows [1:]
scores = []
a_ben = []
b_ben = []
c_ben = []
int_math_score = []
int_art_score = []
value = []

for row in rows:
    split_list = row.split(",")
    value.append(split_list)
print(value)
for r in value:
    score = r[4]
    scores.append(score)
print(scores)
a = scores
step = 3
b = [a[i:i+step] for i in range(0,len(a),step)]#每三个数据分割
print(b)
for l in b:
   ab = l[0]
   bb = l[1]
   cb = l[2]
   a_ben.append(ab)
   b_ben.append(bb)
   c_ben.append(cb)
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
    print(li)
    print("文科")
    print(wen)

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
    #final_list.append(value)
#a_ben.