# Подсчет числа Фибоначчи различными методами
# Для рекурсивных функций формируется файл с деревом вычислений

import os
from recursionvisualisation import CallGraph, viz

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'
cg = CallGraph(filename='Tree.pdf')
cg2 = CallGraph(filename='Tree2.pdf')
@viz(cg)

# Fib1 рекурсивный метод
def Fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)

# Fib2 рекурсивная функция с кэшем
cache = {}
@viz(cg2)
def Fib2(n):
    assert n >= 0
    if n not in cache:
        if n <= 1:
            cache[n] = n
        else:
            cache[n] = fib2(n - 2) + fib2(n - 1)
    return(cache[n])

# Fib3 рекурсивная функция с кэшем
from functools import lru_cache
Fib3 = lru_cache(maxsize=None)(Fib1)

# Fib4 итеративная функция с кэшем
def Fib4(n):
    assert n >= 0
    a,b = 0,1
    for i in range(n - 1):
        a, b = b, a + b
    return(b)

n = int(input())
print(Fib1(n))
