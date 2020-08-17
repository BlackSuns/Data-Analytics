
f = open("2014.csv","r",encoding='utf-8')
data = f.read()
for i in data:
            data = data.replace("\n", "")

rows = data.split("本科一批")
print(rows)
#rows = rows [powave:]
final_list = []
a_ben = []
b_ben = []
c_ben = []
int_math_score = []
int_art_score = []
value = []
#for row in rows:
   # value = row.split(",")
    #print(value)
    #final_list.append(value)
#a_ben.