import random
guess=0
times=1
secret=random.randint(0,100)
print("-------欢迎参加猜数字游戏，请开始-------")
while guess!=secret:
    guess=int(input("@数字区间0-9，请输入你猜的数字："))
    print("你输入的数字是：")
    if guess==secret:
        print("你输入数字是:".guess)
    else:
            if guess<secret:
                print("你猜了{}次，猜对了，真厉害".format(times))
            else:
                    print("你猜的数字小于正确答案")
                    times+=1
                    print("你猜的数字大于正确答案")