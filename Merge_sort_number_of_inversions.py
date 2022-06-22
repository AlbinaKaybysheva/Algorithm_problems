# Первая строка содержит число n, вторая — массив A[1...n],
# содержащий натуральные числа.
# Необходимо посчитать число пар индексов 1 ≤ i < j ≤ n,
# которых A[i] > A[j].


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
    global count
    merged_list = []
    stop_sign = len(list1) + len(list2)
    i1 ,i2 = 0, 0
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
                count += len(list1) - i1
    return merged_list

def Sort(list):
    n1 =2 ** ceil(log(len(list), 2))
    list = [0 for i in range(n1-len(list))] + list
    Q = []
    return MergeAll(Split(list, 0, len(list) - 1, Q))

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    Sort(a)
    print(count)

count = 0
if __name__ == '__main__':
    main()