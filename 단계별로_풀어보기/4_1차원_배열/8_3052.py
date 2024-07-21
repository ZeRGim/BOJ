Li=[]
for i in range(10):
    temp=int(input())
    temp1=temp%42
    Li.append(temp1)
Li=set(Li)
print(len(Li))