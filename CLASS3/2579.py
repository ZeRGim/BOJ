import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
  temp = int(input())
  print(temp)
elif N == 2:
  temp = []
  temp.append(int(input()))
  temp.append(int(input()))
  print(sum(temp))
else:
  stairs = [0]
  for _ in range(N):
    stairs.append(int(input()))
  dp = [0]*(N+1)
  dp[1] = stairs[1]
  dp[2] = stairs[2]
  for i in range(2,N+1):
    dp[i] = max(dp[i-3]+stairs[i]+stairs[i-1],dp[i-2]+stairs[i])
  print(dp[N])