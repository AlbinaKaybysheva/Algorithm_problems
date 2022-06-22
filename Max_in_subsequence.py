# Найти максимум в каждом окне размера m данного массива чисел
# A[1 . . . n].
# Вход: Массив чисел A[1 . . . n] и число 1 ≤ m ≤ n.
# Выход: Максимум подмассива A[i . . . i + m − 1]
# для всех 1 ≤ i ≤ n − m + 1

def MaxInSubsq(lst,m):
    l = 1
    r = m + 1
    lst_max = []
    max_i = max(lst[:m])
    lst_max.append(max_i)
    while r <= len(lst):
        if lst[l - 1] != max_i:
            if lst[r - 1] > max_i:
                max_i = lst[r - 1]
        else:
            max_i = max(lst[l:r])
        lst_max.append(max_i)
        l += 1
        r += 1
    return lst_max

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    m = int(input())
    print(*MaxInSubsq(a, m))

if __name__ == '__main__':
    main()