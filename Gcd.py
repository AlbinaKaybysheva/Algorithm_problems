#Поиск НОД с помощщью Алгоритма Евклида

def GCD(a, b):
    if max(a, b)%min(a,b) == 0: return min(a, b)
    else:
        return GCD(max(a, b)%min(a,b), min(a, b))

x, y = map(int, input().split())
print(GCD(x, y))
