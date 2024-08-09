import sys
input = sys.stdin.readline

dp = [10 for _ in range(50001)]
for i in range(1,224):
  dp[i**2] = 1
n = int(input())
for i in range(2,n+1):
  if dp[i] == 1:
    continue
  else:
    j = 1
    while j**2 <= i:
      dp[i] = min(dp[j**2] + dp[i-(j**2)], dp[i])
      j += 1
print(dp[n])