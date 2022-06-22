# По данным n отрезкам необходимо найти множество точек минимального размера,
# для которого каждый из отрезков содержит хотя бы одну из точек.
# В первой строке дано число n отрезков. Каждая из последующих n строк
# содержит по два числа , задающих начало и конец отрезка.
# Выведите оптимальное число m точек и сами m точек.
# Если таких множеств точек несколько, выведите любое из них.

def SetDots(a, dots):
    if len(a) == 0: return(dots)
    else:
        dots.append(a[0][1])
        for i in reversed(range(1, len(a))):
            if a[i][0] <= a[0][1] <= a[i][1]: a.pop(i)
        a.pop(0)
        return(SetDots(a, dots))

def main():
    n = int(input())
    sec = [[int(j) for j in input().split()] for i in range(n)]
    ans = []
    sec.sort(key = lambda x: x[1])
    print(len(SetDots(sec, ans)))
    print(*SetDots(sec, ans), sep=' ')

if __name__ == '__main__':
    main()
