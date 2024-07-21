N, K= map(int, input().split())
Li=[]
for i in range(N):
    if N % (i+1) == 0:
        Li.append(i+1)
        
try:
    print(Li[K-1])
except:
    print(0)