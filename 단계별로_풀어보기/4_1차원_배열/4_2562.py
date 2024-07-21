Li=[]
for i in range(9):
    temp=int(input())
    Li.append(temp)
maxi=Li[0]
for j in Li:
    if maxi < j:
        maxi=j
whe=int(Li.index(maxi))+1
print(maxi)
print(whe)