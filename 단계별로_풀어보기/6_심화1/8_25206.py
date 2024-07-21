import sys
input=sys.stdin.readline
def cal_sco(x):
    if x=='A+':
        return 4.5
    elif x=='A0':
        return 4.0
    elif x=='B+':
        return 3.5
    elif x=='B0':
        return 3.0
    elif x=='C+':
        return 2.5
    elif x=='C0':
        return 2.0
    elif x=='D+':
        return 1.5
    elif x=='D0':
        return 1.0
    elif x=='F':
        return 0.0
Li=[]
while 1:
    temp=list(input().split())
    if temp == []:
        break
    else:    
        Li.append(temp)
hak=0
sco=0
for i in range(len(Li)):
    if Li[i][2] != 'P':
        hak += float(Li[i][1])
        sco += float(Li[i][1])*float(cal_sco(Li[i][2]))
result=sco/hak
print(result)