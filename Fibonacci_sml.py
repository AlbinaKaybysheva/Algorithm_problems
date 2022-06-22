# Программа для определения времени работы программы вычисляющей
# число Фибоначчи итерационным способом

def Fib(n):
    if n < 2: return(n)
    else:
        fiblist = [0]*(n + 1)
        fiblist[0] = 0
        fiblist[1] = 1
        for i in range(2,n + 1):
            fiblist[i] = fiblist[i-1] + fiblist[i-2]
        return fiblist[n]
N=int(input())
print(Fib(N))

import timeit
code="""
def fib(n):
    if n < 2: return(n)
    else:
        fiblist = [0]*(n  +1)
        fiblist[0] = 0
        fiblist[1] = 1
        for i in range(2,n + 1):
            fiblist[i] = fiblist[i-1] + fiblist[i-2]
        return fiblist[n]
fib(7)
"""
print(timeit.timeit(code,number=1))