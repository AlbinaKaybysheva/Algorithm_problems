# Сортировка слиянием
# На вход подается число n и последовательность из n элементов,
# на выход выводится отсортированная последовательность


from math import log
from math import ceil

def Split(list, l, r, Q):
    if r >= l:
        if l == r:
            Q.append([list[l]])
        else:
            Split(list, l, (l + r) // 2, Q)
            Split(list, (l + r) // 2 + 1, r, Q)
    return Q

def MergeAll(que):
    i = 0
    while i < len(que) - 1:
        que += [Merge(que[i], que[i + 1])]
        i += 2
    return que[len(que) - 1]

def Merge(list1, list2):
    merged_list = []
    stop_sign = len(list1) + len(list2)
    i1, i2 = 0, 0
    while len(merged_list) < stop_sign:
        if i1 == len(list1):
            merged_list += list2[i2:]
        elif i2 == len(list2):
            merged_list += list1[i1:]
        else:
            if list1[i1] <= list2[i2]:
                merged_list.append(list1[i1])
                i1 += 1
            elif list1[i1] > list2[i2]:
                merged_list.append(list2[i2])
                i2 += 1
    return merged_list

def Sort(list):
    n1 =2 ** ceil(log(len(list), 2))
    l1= n1 - len(list)
    list = [0 for i in range(n1-len(list))] + list
    Q = []
    return MergeAll(Split(list, 0, len(list) - 1, Q))[l1:]

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    print(Sort(a))

count = 0
if __name__ == '__main__':
    main()