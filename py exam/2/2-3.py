import random
times=0
guess=0
secret=random.randint(0,100)
maxtimes=eval(input("请输入猜数字的最大次数："))
print("——欢迎参加猜数字游戏——")
for times in range (maxtimes):
    while guess!=secret:
        times+=1
        guess=int(input("数字区间0-100，请输入"))
        print("你输入的数字是：",guess)
        if guess==secret:
            print("你猜了{}次，猜对了，真厉害".format(times))
            break
        else:
            if(guess>secret):
                print("太大了")
                leavetimes=maxtimes-times
                print("你还有{}次机会".format(leavetimes))
            else:
                    print("太小了")
                    leavetimes=maxtimes-times
                    print("你还有{}次机会".format(leavetimes))
                    print("GAME OVER")
                    break