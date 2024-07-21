N = input()
num=[]
for i in range(len(N)):
  num.append(int(N[i]))
num.sort()
num.reverse()
for i in range(len(num)):
  num[i] = str(num[i])
print("".join(num))