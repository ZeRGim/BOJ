N, M= map(int, input().split())
Li=[]
for q in range(1,N+1):
    Li.append(q)
for w in range(M):
    i,j=map(int, input().split())
    temp=Li[i-1:j]
    temp.reverse()
    Li[i-1:j]=temp
for e in range(N):
    print(Li[e], end = ' ')