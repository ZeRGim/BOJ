import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  dp = [1,1,2]
  n = int(input())
  for i in range(3,n+1):
    a = i - 1
    b = i - 2
    c = i - 3
    temp = dp[a] + dp[b] + dp[c]
    dp.append(temp)
  print(dp[n])