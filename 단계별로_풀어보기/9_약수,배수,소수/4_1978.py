n=int(input())

Li=list(map(int, input().split()))
cnt=0
for i in range(n):
    aa=[]
    for j in range(Li[i]):
        if Li[i] % (j+1) == 0:
            aa.append(j+1)
    if len(aa) == 2:
        cnt += 1
        
print(cnt)