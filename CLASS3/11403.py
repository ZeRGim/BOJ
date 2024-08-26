import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
for k in range(n):
  for i in range(n):
    for j in range(n):
      if data[i][k] and data[k][j]:
        data[i][j] = 1

for i in range(n):
  for j in range(n):
    print(data[i][j], end=" ")
  print()