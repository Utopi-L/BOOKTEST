import csv

from sklearn import datasets

def load_data_set():
    with open("E:/VS CodeW/数据挖掘/Groceries.csv",encoding='utf-8') as f:
        f_csv = csv.reader(f)
        for index, val in enumerate(f):
            if index != 0:
                subList = str(val[1]).replace('}','').replace('{','').split(',')
                data_set.append(list(subList))
        return data_set

def create_C1(data_set):
    C1 = set() # 不重复集
    for t in datasets:
        for item in t:
            item_set = frozenset([item]) # item的不可变集合
            C1.add(item_set)
    print("总项数:" + str(len(C1)))
    return C1

def is_apriori(Ck_item, Lksub1):

    for item in Ck_item:
        sub_Ck = Ck_item - frozenset([item])
        if sub_Ck not in Lksub1:
            return False
    return True

def create_Ck(Lksub1, k):

    Ck = set()
    len_Lksub1 = len(Lksub1)
    list_Lksub1 = list(Lksub1)
    for i in range(len_Lksub1):
        for j in range(1, len_Lksub1):
            l1 = list(list_Lksub1[i])
            l2 = list(list_Lksub1[j])
            l1.sort()
            l2.sort()
            if l1[0:k - 2] == l2[0:k - 2]:
                Ck_item = list_Lksub1[i] | list_Lksub1[j]
                # pruning
            if is_apriori(Ck_item, Lksub1):
                Ck.add(Ck_item)
    return Ck

def generate_Lk_by_Ck(data_set, Ck, min_support, support_data):

    Lk = []
    item_count = {}
    for t in data_set: # 遍历所有条目
        for item in Ck: # 候选k阶频繁项集循环
            if item.issubset(t): # item是否是t的子集 ，并计数存到item_count
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1
    t_num = float(len(data_set))
    for item in item_count:
        if (item_count[item] / t_num) >= min_support: # 支持度比较
            print('LK add : ' + str(item))
            Lk.append(item)
            support_data[item] = item_count[item] / t_num
 #print('LK:' + str(Lk))
    return Lk # 返回频繁项集

def generate_L(data_set, k, min_support):

 support_data = {}
 C1 = create_C1(data_set) # 获得一层候选项集
 L1 = generate_Lk_by_Ck(data_set, C1, min_support, support_data) # 获得一层频繁项集
 print("len-lk:" + str(len(list(L1))) + " L1:" + str(L1))
 Lksub1 = L1.copy()
 L = []
 L.append(Lksub1) # List of List
 for i in range(2, k + 1): # 多层频繁项集的获取
    Ci = create_Ck(Lksub1, i)
    Li = generate_Lk_by_Ck(data_set, Ci, min_support, support_data)
    Lksub1 = Li.copy()
    L.append(Lksub1)
 return L, support_data # L是所有的频繁项集，按照层数保存的List of List，support_data是频繁项集和支持度的键值对

def generate_big_rules(L, support_data, min_conf):

    big_rule_list = []
    sub_set_list = []
    for i in range(0, len(L)): # 遍历频繁项集
        for freq_set in L[i]: # 频繁项集
            for sub_set in sub_set_list:
                if sub_set.issubset(freq_set):
                    # print("sub_set:" + str(sub_set))
                    # print("freq_set:" + str(freq_set))
                    conf = support_data[freq_set] / support_data[freq_set - sub_set] # 支持度计算
                    big_rule = (freq_set - sub_set, sub_set, conf)
                    # print("freq_set - sub_set:" + str(freq_set - sub_set))
                    if conf >= min_conf and big_rule not in big_rule_list:
                        # print freq_set-sub_set, " => ", sub_set, "conf: ", conf
                        big_rule_list.append(big_rule)
            sub_set_list.append(freq_set)
    return big_rule_list

if __name__ == "__main__":

 data_set = load_data_set()
 L, support_data = generate_L(data_set, k=3, min_support=0.02) # L是所有的频繁项集，按照阶数保存的List of List，support_data是频繁项集和支持度的键值对，K=3则最高取到三层
 big_rules_list = generate_big_rules(L, support_data, min_conf=0.3)
 for Lk in L:
    print("=" * 50)
 print("***" + str(len(list(Lk))))
 print("frequent " + str(len(list(Lk)[0])) + "-itemsets\t\tsupport")
 print("=" * 50)
 for freq_set in Lk:
    print(freq_set, support_data[freq_set])
 print()
 print("Big Rules")
 for item in big_rules_list:
  print(item[0], "=>", item[1], "conf: ", item[2])
