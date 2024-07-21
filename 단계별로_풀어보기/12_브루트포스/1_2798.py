n,m=map(int,input().split())
List=list(map(int,input().split()))
sumlist=[]
eum=[]
for i in List:
    for j in List:
        if j==i:
            continue
        for k in List:
            if k==j or k==i:
                continue
            sumlist.append(i+j+k)
for i in range(len(sumlist)):
    if sumlist[i] - m > 0:
        pass
    else:
        eum.append(sumlist[i] - m)
for i in range(len(eum)):
    eum[i] = -1*eum[i]
key=min(eum)
print(m-key)