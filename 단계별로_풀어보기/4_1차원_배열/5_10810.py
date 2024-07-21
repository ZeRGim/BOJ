N,M = map(int, input().split())
Li=[]
for qwe in range(N):
    Li.append('0')
for soo in range(M):
    i,j,k=map(int, input().split())
    for _ in range(i,j+1):
        Li[_-1]=str(k)

result=" ".join(Li)
print(result)