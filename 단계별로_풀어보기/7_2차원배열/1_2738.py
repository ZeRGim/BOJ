def r(i,M):
    global result
    result=[]
    for w in range(M):
        result.append(int(hang1[i][w])+int(hang2[i][w]))
    return result
N,M= map(int, input().split())
hang1=[]
hang2=[]
result_=[]
for i in range(N):
    hang1.append(list(input().split()))
for i in range(N):
    hang2.append(list(input().split()))
for i in range(N):
    result_.append(r(i,M))
for i in range(N):
    for j in range(M):
        print(result_[i][j], end=" ")
    print("")