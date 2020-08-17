f=open("C:/360极速浏览器下载/dq_unisex_names.csv","r",encoding='utf-8')
data=f.read()
rows=data.split('\n')
print(rows)
name=[]
for row in rows:
    value=row.split(',')
    count=value[1]
    if float(count)>=1000:
        name.append(value[0])
print(name)