import csv
import pandas
f = open("course.csv",'r',encoding='utf-8')
csvreader = csv.reader(f)
new = list (csvreader)
new = new [1:]
print(new)
for i in new:
    if i not in new:
        new.append(i)
course = []
tens=[]
people = []
price = []
for i in course[0:10]:
    value = i [0]
    tens.append(value)
max_price = 0
max_people = 0
for i in new:
    value = i [2]
    if float(max_price) < float(value):
        max_price = value
    price.append(float(value))
print(max_price)

print (price)
for i in new:
    value = i [3]
    if int(max_people) < int(value):
        max_people = value
    people.append(int(value))
print(max_people)
print (people)
for i in new:
    if i[2] == max_price:
        print("课程价格最高为:" + str(i[0]))
for i in new:
    if i[3] == max_people:
        print("学习人数最多的课程为:" + str(i[0]))