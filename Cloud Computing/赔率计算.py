
from time import time
import math


def is_prime(x):
    return 0 not in [x % i for i in range(2, int(math.sqrt(x)) + 1)]


def is_prime3(x):
    flag = True
    for p in p_list2:
        if p > math.sqrt(x):
            break
        if x % p == 0:
            flag = False
            break
    if flag:
        p_list2.append(x)
    return flag


if __name__ == "__main__":

    a = 2
    b = 10000

    '''统计五种方法的计算时间'''
    # 方法1：直接计算
    t = time()
    p = [p for p in range(a, b) if 0 not in [p % d for d in range(2, int(math.sqrt(p)) + 1)]]
    print(time() - t)
    print(p)

    # 方法2：利用filter(与方法1类似)
    # filter() 函数用于过滤序列，过滤掉不符合条件的元素,该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
    t = time()
    # 调用is_prime
    p = filter(is_prime, range(a, b))
    print(time() - t)
    print(list(p))

    # 方法3：利用filter和lambda(与方法1类似)
    t = time()
    # lambda 匿名函数
    is_prime2 = (lambda x: 0 not in [x % i for i in range(2, int(math.sqrt(x)) + 1)])
    p = filter(is_prime2, range(a, b))
    print(time() - t)
    print(list(p))

    # 方法4：定义
    t = time()
    p_list = []
    for i in range(2, b):
        flag = True
        for p in p_list:
            if p > math.sqrt(i):
                break
            if i % p == 0:
                flag = False
                break
        if flag:
            p_list.append(i)
    print(time() - t)
    print(p_list)

    # 方法5：定义和filter(与方法4类似)
    p_list2 = []
    t = time()
    # 调用is_prime3
    p = filter(is_prime3, range(2, b + 1))
    print(time() - t)
    print(list(p))

    print('---------------------')
    a = 750
    b = 900
    p_train = filter(is_prime3, range(2, b + 1))  # 定义为数组
    p_trainvalue = list(p_train)
    print('---------------------')
    # 搜索在指定范围内的素数
    p_train = [p_trainvalue[x] for x in range(len(p_trainvalue)) if p_trainvalue[x] >= a]
    print(p_train)
    # 计算在指定范围内素数的概率
    p_rate = float(len(p_train)) / float(b - a + 1)
    print('素数的概率：', p_rate, '\t', )
    print('公正赔率：', 1 / p_rate)
    print('合数的概率：', 1 - p_rate, '\t', )
    print('公正赔率：', 1 / (1 - p_rate))
