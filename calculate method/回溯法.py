import numpy as np

weight = [0, 2, 5, 4, 2]
value = [0, 6, 3, 5, 4]
flag = np.full(len(value), False)
W = 10
bestV = 0
bestX = flag
cv = 0
cw = 0

def back(k):
    global maxV, cv, cw, bestV

    if k >= len(value):
        if cv > bestV:
            for i in range(1, len(value)):
                bestX[i] = flag[i]

            bestV = cv

            return

    if cw + weight[k] <= W:    #判断左子树是否符合条件
        flag[k] = True
        cw += weight[k]
        cv += value[k]
        back(k+1)
        cv -= value[k]
        cw -= weight[k]

    if (bound(k+1, cv) > bestV):   #右子树
        flag[k] = False
        back(k+1)


def bound(k, cv):
    rv = 0

    while(k < len(value)):
        rv += value[k]
        k += 1

    return cv + rv

if __name__ == '__main__':
    back(1)
    print(bestV)
