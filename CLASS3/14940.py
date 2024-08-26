import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())

graph = [list(map(int, input().strip().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
def bfs(x,y):
  dx = [0,0,-1,1]
  dy = [-1,1,0,0]
  queue = deque([[x,y]])
  while queue:
    select = queue.popleft()
    for i in range(4):
      nx = select[0] + dx[i]
      ny = select[1] + dy[i]
      if 0<=nx<m and 0<=ny<n and graph[ny][nx] and not visited[ny][nx]:
        visited[ny][nx] = 1
        graph[ny][nx] += graph[select[1]][select[0]]
        queue.append([nx,ny])
  else:
    for i in range(n):
      for j in range(m):
        if not visited[i][j]:
          if graph[i][j] == 0:
            pass
          else:
            graph[i][j] = -1
def finding_start(graph):
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 2:
        return [j,i]

xy = finding_start(graph)
graph[xy[1]][xy[0]] = 0
bfs(*xy)

for i in range(n):
  for j in range(m):
    print(graph[i][j], end=" ")
  print()