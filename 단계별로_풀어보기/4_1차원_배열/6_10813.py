N, M = map(int, input().split())
Li=[]
for i in range(1,N+1):
    Li.append(str(i))
for cnt in range(M):
    i,j= map(int, input().split())
    Li[i-1], Li[j-1]= Li[j-1], Li[i-1]
result=" ".join(Li)
print(result)