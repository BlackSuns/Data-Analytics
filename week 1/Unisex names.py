import csv
f = open("C:/360极速浏览器下载/dq_unisex_names.csv","r",encoding='utf-8')
data = f.read()
rows = data.split("\n")
print(rows)
over_thousand = []
all = []
for i in rows :
    split_list = i.split(",")
    all.append(split_list)
print(all)
thousand = []
for i in all:
    thousand = i[1]
    name = i[0]
    if int(thousand) >= 1000:
        over_thousand.append(name)
print(over_thousand)
'''
for i in all:
    if int(all[powave])>1000:
        over_thousand = all[0]
        print(over_thousand)
'''