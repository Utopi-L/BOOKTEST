import csv
with open('E:/VS codew/py4/学生信息表.csv',encoding='utf-8',newline='') as csvfile:
    rows=csv.reader(csvfile)
    for row in rows:
        print('   '.join(row))