import turtle
from unittest import result
def main():
    turtle.setup(800,600,0,0)
    turtle.pencolor("red")
    turtle.width(5)
    turtle.speed(5)
    result=[]
    file=open("E:/VS codew/200511437py4/2.py/data.txt","r")
    for line in file:
        result.append(list(map(float,line.split(','))))
    print(result)
    for i in range(len(result)):
        turtle.pencolor((result[i][3],result[i][4],result[i][5]))
        turtle.forward(result[i][0])
        if result[i][1]:
            turtle.rt(result[i][2])       
        else:
            turtle.lt(result[i][2])
    turtle.done()
main()