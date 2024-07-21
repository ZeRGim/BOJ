Li=[]
for i in range(30):
    Li.append(i+1)

for j in range(28):
    submit=int(input())
    Li.remove(submit)
Li.sort()
print(Li[0])
print(Li[1])