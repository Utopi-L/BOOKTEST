import json
import csv

fr=open("E:/VS codew/py4/学生信息表.csv","r")
ls=[]
for line in fr:
    line=line.replace("\n","")
    ls.append(line.split(","))
fr.close()
fw=open("E:/VS codew/py4/学生信息表.json","w")
for i in range(1,len(ls)):
    ls[i]=dict(zip(ls[0],ls[i]))
b = json.dumps(ls[1:],sort_keys=True,indent=4,ensure_ascii=False)
print(b)
fw.write(b)
fw.close()