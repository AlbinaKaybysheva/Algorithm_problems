# Нахождение наибольшей невозрастающей подпоследовательности
# На вход подается число n и последовательность из n элементов,
# на выход выводится количество элементов в наибольшей невозрастающей
# подпоследовательности и индексы элементов этой подпоследовательности

def DecreaseSubsequence(A):
    n = len(A)
    num = [1 for i in range(n)]
    n_max = 1
    i_max = 0
    index = [-1 for i in range(n)]
    for i in range(n):
        for j in range(0, i):
            if A[i] <= A[j] and num[i] < num[j] + 1:
                num[i] = num[j] + 1
                index[i] = j
                if num[i] >= n_max:
                    n_max = num[i]
                    i_max = i
    row = [0 for i in range(n_max + 1)]
    row[0] = n_max
    prev = i_max
    for j in range(n):
        i = n - 1 - j
        if i == prev:
            row[n_max] = i + 1
            n_max -= 1
            prev = index[i]
    return row


def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ds = DecreaseSubsequence(a)
    print(ds[0])
    print(*ds[1:])

def test(): # проверка основых случаев
    assert DecreaseSubsequence([5, 3, 4, 4, 2]) == [4, 1, 3, 4, 5]
    assert DecreaseSubsequence([1]) == [1, 1]
    assert DecreaseSubsequence([1, 2, 6]) == [1, 1]
    assert DecreaseSubsequence([1, 1, 1]) == [3, 1, 2, 3]
    assert DecreaseSubsequence([1, 0, 0, 0, 0, 1]) == [5, 1, 2, 3, 4, 5]
    assert DecreaseSubsequence([9, 9, 10, 10]) == [2, 3, 4]


if __name__ == '__main__':
    main()
    #test()