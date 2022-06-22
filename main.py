s_raw=[i for i in input()]
s=[]
num=[]
for i in range(len(s_raw)):
    if s_raw[i] in ['(',')','[',']','{','}']:
        s.append(s_raw[i])
        num.append(i)
s2=[]
num2=[]
while len(s)>1:
    s2.append(s[len(s)-1])
    num2.append(num[len(num)-1])
    s.pop(len(s)-1)
    num.pop(len(num)-1)
    while (len(s)>0 and len(s2)>0 and ((s[len(s)-1]=='(' and s2[len(s2)-1]==')') or (s[len(s)-1]=='[' and s2[len(s2)-1]==']') or (s[len(s)-1]=='{' and s2[len(s2)-1]=='}')))==1:
        s.pop(len(s)-1)
        s2.pop(len(s2)-1)
        num.pop(len(num)-1)
        num2.pop(len(num2)-1)
if len(s)==0 and len(s2)==0: print('Success')
else:
    k=-1
    for i in range(len(s2)):
        if s2[i] in [')',']','}']: k=num2[i]
    if len(s)!=0 and s[0] in [')',']','}']: k=num[0]
    if k!=-1: print(k+1)
    else:
        for i in reversed(range(len(s2))):
            if s2[i] in ['(', '[', '{']: k = num2[i]
        if len(s2)==0 and s[0] in ['(', '[', '{']: k = num[0]
        print(k+1)