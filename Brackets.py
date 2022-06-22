# На вход подается текст, содержащий скобки (, ), [, ], {, }.
# Программа должна проверить правильность расствления скобок.
# Если скобки расставлены правильно, выводится строка “Success".
# В противном случае выводится индекс (используя индексацию с единицы) первой ошибки.

s_raw=[i for i in input()]
s=[] # Массив содержит только скобки по порядку следования
num=[]
for i in range(len(s_raw)):
    if s_raw[i] in ['(', ')', '[', ']', '{', '}']:
        s.append(s_raw[i])
        num.append(i)
s2=[] # Массив для реализации стека
num2=[] #Массив для запоминания индекса скобок в исходном тексте
while len(s) > 1:
    s2.append(s[len(s)-1])
    num2.append(num[len(num)-1])
    s.pop(len(s)-1)
    num.pop(len(num)-1)
    while (len(s) > 0 and len(s2) > 0 and ((s[len(s)-1] == '(' and s2[len(s2)-1] == ')') or
                                           (s[len(s)-1] == '[' and s2[len(s2)-1] == ']') or
                                           (s[len(s)-1] == '{' and s2[len(s2)-1] == '}'))) == 1:
        s.pop(len(s)-1)
        s2.pop(len(s2)-1)
        num.pop(len(num)-1)
        num2.pop(len(num2)-1)
if len(s) == 0 and len(s2) == 0: print('Success')
else: # Поиск индекса первой ошибки
    k=-1
    for i in range(len(s2)):
        if s2[i] in [')',']','}']: k=num2[i]
    if len(s)!=0 and s[0] in [')', ']', '}']: k=num[0]
    if k!=-1: print(k+1)
    else:
        for i in reversed(range(len(s2))):
            if s2[i] in ['(', '[', '{']: k = num2[i]
        if len(s2)==0 and s[0] in ['(', '[', '{']: k = num[0]
        print(k+1)