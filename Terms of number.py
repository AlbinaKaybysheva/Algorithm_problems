# По данному числу n найдите максимальное число k,
# для которого n можно представить как сумму
# k различных натуральных слагаемых.
# Выведите в первой строке число k, во второй — k слагаемых.

def Terms(n):
    balance = n
    i = 1
    trm = []
    while i < balance/2:
        balance -= i
        trm.append(i)
        i +=1
    trm.append(balance)
    return trm

n=int(input())
print(len(Terms(n)))
print(*Terms(n))
