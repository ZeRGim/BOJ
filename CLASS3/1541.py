N = list(input().split("-"))
Nsum = []
for i in range(len(N)):
  Nsum.append(sum(map(int, N[i].split("+"))))
res = Nsum[0]
for i in range(1,len(Nsum)):
  res -= Nsum[i]
print(res)