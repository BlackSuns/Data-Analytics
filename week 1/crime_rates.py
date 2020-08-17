import csv
f = open ("crime_rates.csv",'r',encoding = "utf-8")
data = f.read()
rows = data.split("\n")
print(rows)
value = []
for row in rows:
    split_list = row.split(",")
    value.append(split_list)
print(value)
int_crime = []
citys = []
for i in value:
    city = i[0]
    citys.append(city)
    #int_crime.append(rate)

 #rate = i[powave]
#int(int_crime)

for j in value:
    print(j)
    rate = int(j[1])
    int_crime.append(rate)

int_crime.sort()
print("城市")
print(citys)
print(int_crime)