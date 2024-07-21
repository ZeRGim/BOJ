Li=[]
for i in range(5):
  Li.append(int(input()))
Li.sort()
print(sum(Li)//5)
print(Li[2])