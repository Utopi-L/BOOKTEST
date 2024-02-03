import random

from sqlalchemy import true
allList=['石头','剪刀','布']
winList=[['石头','剪刀'],['剪刀','布'],['布','石头']]
chnum=-1
prompt='''
===欢迎参加石头剪刀布游戏===

请选择：
0 石头
1 剪刀
2 布
3 我不想玩了

===========================
请选择对应的数字：'''
while True:
    chnum = input(prompt)
    if chnum not in ['0','1','2','3']:
        print("无效的选择，请选择 0/1/2/3")
        continue
    if chnum == '3':
        break
    cchoice =random.choice(allList)
    uchoice =allList[int(chnum)]
    print("你选择了：{}\n计算机选择了：{}".format(uchoice,cchoice))
    if uchoice == cchoice:
        print("平局")
    elif [uchoice,cchoice] in winList:
            print("你赢了！！！")
    else:
            print("你输了!!!")
print("游戏结束!")