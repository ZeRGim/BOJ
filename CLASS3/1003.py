import sys
input = sys.stdin.readline

T = int(input())

DP = [[]]*41
DP[0] = [1,0]
DP[1] = [0,1]
for i in range(2,41):
  DP[i] = [DP[i-1][0]+DP[i-2][0], DP[i-1][1]+DP[i-2][1]]
for _ in range(T):
  N = int(input())
  print(DP[N][0], DP[N][1])
