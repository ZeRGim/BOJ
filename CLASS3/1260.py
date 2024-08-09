import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int,input().split())
maps = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, input().split())
  maps[a][b] = maps[b][a] = 1
visited1 = [0]*(N+1)
visited2 = visited1.copy()

def dfs(x):
  visited1[x] = 1
  print(x, end=" ")
  for i in range(1,N+1):
    if maps[x][i] == 1 and visited1[i] == 0:
      dfs(i)

def bfs(x):
  queue = deque([x])
  visited2[x] = 1
  while queue:
    temp = queue.popleft()
    print(temp, end=" ")
    for i in range(1,N+1):
      if maps[temp][i] == 1 and visited2[i] == 0:
        queue.append(i)
        visited2[i] = 1

dfs(V)
print()
bfs(V)