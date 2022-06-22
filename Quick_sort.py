# Быстря сортировка массива с предварительной сортировкой
# На вход подается число n и последовательность из n элементов,
# на выход выводится отсортированная последовательность


def QuickSort(A, l, r):
    if l < r:
            m = Partition(A, l, r)
            QuickSort(A, l, m - 1)
            QuickSort(A, m + 1, r)
    return A

# разделение массива на два, с элементами A[l], >A[l] и <A[l]
def Partition(A, l, r):
    x = A[l]
    j = l
    for i in range(l + 1, r + 1):
        if A[i] <= x:
            j += 1
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def main():
    a = [int(i) for i in input().split()]
    print(QuickSort(a, 0, len(a) - 1))

if __name__ == '__main__':
    main()