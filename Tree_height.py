# Вычислить высоту данного дерева.
# Вход: Корневое дерево с вершинами {0, . . . , n−1}, заданное
# как последовательность parent0, . . . , parentn−1
# , где parenti — родитель i-й вершины.
# Выход: высота данного дерева


def TreeHeight(a):
    height = 1
    a_tmp = a + [int(i) for i in range(len(a))]
    H = dict(zip(set(a_tmp), [-1 for i in range(len(set(a_tmp)))]))
    height = TreeHeightR(a, -1, height, H)
    return height

def TreeHeightR(a, root, h, H):
    n = len(a)
    h = 0
    if H[root] != -1:
        h = H[root]
    else:
        for i in range(n):
            if a[i] == root:
                h = max(h, TreeHeightR(a, i, h, H) + 1)
        H[root] = h
    return h

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    print(TreeHeight(a))

if __name__ == '__main__':
    main()