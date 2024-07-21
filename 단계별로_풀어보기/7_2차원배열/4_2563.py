Li=[]

for i in range(100):
    temp=[]
    for j in range(100):
        temp.append(0)
    Li.append(temp)
N= int(input())

for i in range(N):
    x,y= map(int, input().split())
    for a in range(x,x+10):
        for b in range(y,y+10):
            Li[a][b] += 1
cnt=0
for i in range(100):
    for j in range(100):
        if Li[i][j] != 0:
            cnt += 1
print(cnt)