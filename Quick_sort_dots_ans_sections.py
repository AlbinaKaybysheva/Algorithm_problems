

def QuickSort(A, n, l, r):
    if l < r:
            m = Partition(A, n, l, r)
            QuickSort(A ,n, l, m - 1)
            QuickSort(A ,n , m + 1, r)
    return A

def Partition(A, n, l, r):
    x = A[l][n]
    j = l
    for i in range(l + 1, r + 1):
        if A[i][n] <= x:
            j += 1
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def DotsInSections(sec, dots):
    Start = SectionsEdge(sec, 0)
    End = SectionsEdge(sec, 1)
    n_starts, n_ends = 0, 0
    t = []
    for dot in dots:
        for st in Start:
            if st > dot: n_starts += 1
        for end in End:
            if end < dot: n_ends += 1
        print('проверяю', dot, 'st, end = ', n_starts, n_ends)
        if n_starts + n_ends < len(Start):
            t += [len(Start) - n_starts - n_ends]
        else:
            t += [0]
    return t

def BinarySearch(value, list_of_elements, n):
    pl = -1
    start = 0
    end = len(list_of_elements) - 1
    while pl == -1 and (end - 1 > start):
        mid = ((end + start) + (end + start) % 2) // 2
        if value == list_of_elements[mid][n]:
            pl = mid
            while list_of_elements[pl - 1][n] == value and pl > 0:
                pl -= 1
            pl += 1
        elif value > list_of_elements[mid][n]:
            start = mid + 1
        else:
            end = mid
    if ((start + 1) == end or start == end) and list_of_elements[start][n] == value: pl = start + 1
    if (start + 1) == end and list_of_elements[end][n] == value: pl = end + 1
    return pl

def main():
    a = []
    t = [int(i) for i in input().split()]
    while len(t) == 2:
        a += [t]
        t = [int(i) for i in input().split()]



if __name__ == '__main__':
    #main()
    a = [[1, 2], [2, 5], [4, 3], [2,10]]
    a.sort(key = lambda x: x[1])
    print(QuickSort(a, 0, 0, len(a) - 1))
    print(QuickSort(a, 1, 0, len(a) - 1))
    print(BinarySearch())

