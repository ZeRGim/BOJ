now=list(map(int, input().split()))
right=[1, 1, 2, 2, 2, 8]
result=[]
for i in range(len(right)):
    res=right[i]-now[i]
    result.append(res)
for i in range(len(result)):
    print(result[i], end=" ")