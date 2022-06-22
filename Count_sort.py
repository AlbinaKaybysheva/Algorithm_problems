# Сортировка подсчетом
# На вход подается число n и последовательность из n элементов,
# на выход выводится отсортированная последовательность

def CountSort(A):
    n = len(A)
    B = [0 for i in range(11)]
    A_sorted = []
    for el in A:
        B[el] += 1
    for i in range(10):
        A_sorted += [i + 1] * B[i + 1]
    return A_sorted

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    print(CountSort(a))

if __name__ == '__main__':
    main()