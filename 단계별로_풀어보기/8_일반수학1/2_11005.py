N,B=map(int, input().split())
Li=[]
while N>0:
    Li.append(N%B)
    N = N//B

for i in range(len(Li)):
    if 10<=Li[i]<B:
        Li[i]=chr(Li[i]+55)

Li.reverse()

for j in Li:
    print(j, end="")