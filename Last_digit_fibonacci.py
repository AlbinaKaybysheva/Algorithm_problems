# Вычисление последней цифры n-ного числа Фибоначчи
# последняя цифра числа Фибоначчи равно остатку от деления на 10
# суммы последних цифр двух предыдущих чисел

def FibLastDigit(n):
    d1 = 0
    d2 = 1
    if n > 1:
        for i in range(2,n + 1):
            temp = (d1 + d2)%10
            d1 = d2
            d2 = temp
    return d2

N = int(input())
print(FibLastDigit(N))