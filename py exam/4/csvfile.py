import csv
import weakref
csvfile = open('E:/VS codew/py4/学生信息表.csv',"a+",encoding='utf-8')
writer =csv.writer(csvfile)
writer.writerow(['17010002','赵四','女','自动化1701'])
csvfile.close()