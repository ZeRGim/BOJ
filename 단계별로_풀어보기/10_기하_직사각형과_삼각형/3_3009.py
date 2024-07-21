first=list(map(int, input().split()))
secon=list(map(int, input().split()))
third=list(map(int, input().split()))
items=[first,secon,third]
x=[]
y=[]
res=[]
for i in range(3):
    x.append(items[i][0])
for i in range(3):
    y.append(items[i][1])
if x[0] == x[1]:
    res.append(x[2])
elif x[0] == x[2]:
    res.append(x[1])
elif x[2] == x[1]:
    res.append(x[0])
if y[0] == y[1]:
    res.append(y[2])
elif y[0] == y[2]:
    res.append(y[1])
elif y[2] == y[1]:
    res.append(y[0])
print(res[0], res[1])
