# Реализация обхода дерева
# Вход: Корневое дерево с вершинами {0, . . . , n−1}, заданное
# как последовательность parent0, . . . , parentn−1
# , где parenti — родитель i-й вершины.
# Выход: последовательность вершин данного дерева


def TreeTraversal(a):
    etalon = -1
    TreeTraversalRoot(a, etalon)

def TreeTraversalRoot(a, etalon):
    for i in range(len(a)):
        if a[i] == etalon:
            print(i)
            TreeTraversalRoot(a, i)

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    print(TreeTraversal(a))

if __name__ == '__main__':
    main()