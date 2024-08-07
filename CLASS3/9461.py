import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  basic = [0,1,1,1,2,2]
  n = int(input())
  if n <= 5:
    print(basic[n])
    continue
  else:
    for i in range(6,n+1):
      basic.append(basic[i-5] + basic[i-1])
    print(basic[n])