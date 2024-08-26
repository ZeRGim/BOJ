import sys
input = sys.stdin.readline
from collections import deque
m,n= map(int, input().split())
graph = [list(map(int,input().split())) for i in range(n)]
visited = [[0]*m for _ in range(n)]
def bfs():
  queue = deque([])
  for j in range(n):
    for k in range(m):
      if graph[j][k] == 1:
        queue.append([j,k])
      if graph[j][k] == -1:
        visited[j][k] = 1
  dx = [0,0,1,-1]
  dy = [1,-1,0,0]
  while queue:
    select = queue.popleft()
    visited[select[0]][select[1]] = 1
    for i in range(4):
      nx = select[1] + dx[i]
      ny = select[0] + dy[i]
      
      if 0<=nx<m and 0<=ny<n:
        if not visited[ny][nx]:
          visited[ny][nx] = 1
          if graph[ny][nx] == 0:
            graph[ny][nx] = graph[select[0]][select[1]] + 1
            queue.append([ny,nx])
  else:
    try:
      return graph[select[0]][select[1]]
    except:
      return 0
def check_complete():
  for j in range(n):
    for k in range(m):
      if visited[j][k] == 0:
        return False
  else:
    return True

max_ = bfs() - 1
if check_complete():
  print(max_)
else:
  print("-1")