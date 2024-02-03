from itertools import count
import jieba
excludes ={"不过","的话","不好","姐姐","一时","不能","过来","出去","所以","不敢","这些","丫头","只得","老爷","大家","回来","东西","告诉","就是","咱们","什么","只是","如此","看见",'一个',"我们","那里","你们","如今","说道","知道","老太太","起来","姑娘","这里","出来","他们","众人","自己","一面","太太","只见","怎么","奶奶","两个","没有","不是","不知","这个","听见","这样","进来"}
txt = open("D:/QQ/1341708786/FileRecv/红楼梦.txt","r",encoding='utf-8').read()
words =jieba.lcut(txt)
counts={}
for word in words:
    if len(word) == 1:
        continue
    elif word=="林黛玉" or word == "林姑娘" :
        rword = "林黛玉"

    else:
        rword = word
        counts[rword]=counts.get(rword,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))