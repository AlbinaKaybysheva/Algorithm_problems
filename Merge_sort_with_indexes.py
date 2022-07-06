# Сортировка слиянием
# На вход подается число n и последовательность из n элементов,
# на выход выводится отсортированная последовательность


from math import log
from math import floor

# def Split(list, l, r, Q):
#     if r >= l:
#         if l == r:
#             Q.append([list[l]])
#         else:
#             Split(list, l, (l + r) // 2, Q)
#             Split(list, (l + r) // 2 + 1, r, Q)
#     return Q
#
# def MergeAll(que):
#     i = 0
#     while i < len(que) - 1:
#         que += [Merge(que[i], que[i + 1])]
#         i += 2
#     return que[len(que) - 1]

def Merge(A, p, q, r):
    p -= 1 # привожу номер элемента массива к виду согласно примеру запуска
    q -= 1 # (нумерация элементов начинается с 1)
    r -= 1
    merged_list = []
    stop_sign = r - p + 1
    i1, i2 = p, q + 1
    while len(merged_list) < stop_sign:
        #print(merged_list)
        if i1 == q + 1:
            merged_list += A[i2:r + 1]
        elif i2 == r + 1:
            merged_list += A[i1:q + 1]
        else:
            if A[i1] <= A[i2]:
                merged_list.append(A[i1])
                i1 += 1
            elif A[i1] > A[i2]:
                merged_list.append(A[i2])
                i2 += 1
    A[p:r + 1] = merged_list
    return A

def Sort(list, p, r):
    if p < r:
        q = floor((p + r) / 2)
        Sort(list, p, q)
        Sort(list, q + 1, r)
        Merge(list, p, q, r)
    return list

def main():
    # n = int(input())
    # a = [int(i) for i in input().split()]
    a = [5, 2, 4, 6, 1, 3, 2, 6]
    print(Sort(a, 1, len(a)))

count = 0
if __name__ == '__main__':
    main()