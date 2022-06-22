# В первой строке даны целое число n и массив A[1…n]
# из n различных натуральных чисел в порядке возрастания,
# во второй — целое число k и k натуральных чисел b_1 ... b_k.
# Для каждого i от 1 до k необходимо вывести индекс
# 1 ≤ j ≤ n, для которого A[j] = b_i или −1, если такого j нет.


def BinarySearch(value, list_of_elements):
    pl = -1
    start = 0
    end = len(list_of_elements) - 1
    while pl == -1 and (end - 1 > start):
        mid = ((end + start) + (end + start) % 2) // 2
        if value == list_of_elements[mid]:
            pl = mid
            while list_of_elements[pl - 1] == value and pl > 0:
                pl -= 1
            pl += 1
        elif value > list_of_elements[mid]:
            start = mid + 1
        else:
            end = mid
    if ((start + 1) == end or start == end) and list_of_elements[start] == value: pl = start + 1
    if (start + 1) == end and list_of_elements[end] == value: pl = end + 1
    return pl

def main():
    etalon_list = [int(i) for i in input().split()[1:]]
    example_list = [int(i) for i in input().split()[1:]]
    for el in example_list:
        print(BinarySearch(el, etalon_list), end=' ')

if __name__ == '__main__':
    main()
