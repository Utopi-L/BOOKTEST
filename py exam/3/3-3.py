
import jieba
txt ='''
卜算子
【宋】李之仪
我住长江头，君住长江尾。
日日思君不见君，共饮长江水。
此水几时休？此恨何时了？
只愿君心似我心，定不负相思意。
'''
words = jieba.lcut(txt)
print(words)
counts={}
for word in words:
    if len (word) == 1:
        continue
    else:
        rword = word
        counts[rword] =counts.get(rword,0) +1
print(counts)
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for item in items:
    print(item)
for item in items:
    word, count =item
    print ("{0:<10}{1:>5}".format(word,count))