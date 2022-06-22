# Первая строка содержит количество предметов и вместимость рюкзака.
# Каждая из следующих n строк задаёт стоимость и объём предмета — целые числа).
# Программа выводит максимальную стоимость частей предметов
# (от каждого предмета можно отделить любую часть, стоимость и объём при этом
# порционально уменьшатся), помещающихся в данный рюкзак,
# с точностью не менее трёх знаков после запятой

def BagFilling(Volume, list_of_subjects):
    list_of_subjects.sort(key=lambda x: x[0]/x[1], reverse=True)
    fil, price, i = 0, 0, 0
    while fil < Volume and i < len(list_of_subjects):
        if (fil + list_of_subjects[i][1]) < Volume:
            fil += list_of_subjects[i][1]
            price += list_of_subjects[i][0]
        else:
            price += list_of_subjects[i][0]*(Volume-fil)/list_of_subjects[i][1]
            fil = Volume
        i += 1
    return(price)

n, Vol = map(int, input().split())
elements = [[int(j) for j in input().split()] for i in range(n)]
print('%.3f' % BagFilling(Vol, elements))