import sys
input = sys.stdin.readline

n = int(input())
DP = {0:0, 1:0}

for i in range(2,n+1):
  temp = []
  temp.append(DP[i-1] + 1)
  if i % 2 == 0:
    temp.append(DP[i//2] + 1)
  if i % 3 == 0:
    temp.append(DP[i//3] + 1)
  DP[i] = min(temp)
print(DP[n])