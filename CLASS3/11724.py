import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0]*(N+1) for i in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = 1
visited = [0]*(N+1)
cnt = 0

def bfs(x):
  global cnt
  queue = deque([x])
  visited[x] = 1
  while queue:
    temp = queue.popleft()
    for i in range(1,N+1):
      if graph[temp][i] == 1 and visited[i] == 0:
        queue.append(i)
        visited[i] = 1
  cnt += 1

for i in range(1,N+1):
  if visited[i] == 0:
    bfs(i)
print(cnt)