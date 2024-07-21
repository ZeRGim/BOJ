import sys
N,X=map(int, sys.stdin.readline().split())

Li=list(sys.stdin.readline().split())
result=[]
for i in Li:
    if int(i)<X:
        result.append(i)

b=" ".join(result)
print(b)