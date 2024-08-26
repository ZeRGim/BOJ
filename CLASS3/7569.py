import sys
input = sys.stdin.readline
from collections import deque
m,n,h = map(int, input().split())
graph = [[list(map(int,input().split())) for i in range(n)] for j in range(h)]
visited = [[[0]*m for _ in range(n)] for i in range(h)]
def bfs():
  queue = deque([])
  for i in range(h):
    for j in range(n):
      for k in range(m):
        if graph[i][j][k] == 1:
          queue.append([i,j,k])
        if graph[i][j][k] == -1:
          visited[i][j][k] = 1
  dx = [0,0,0,0,1,-1]
  dy = [0,0,1,-1,0,0]
  dz = [1,-1,0,0,0,0]
  
  while queue:
    select = queue.popleft()
    visited[select[0]][select[1]][select[2]] = 1
    for i in range(6):
      nx = select[2] + dx[i]
      ny = select[1] + dy[i]
      nz = select[0] + dz[i]
      
      if 0<=nx<m and 0<=ny<n and 0<=nz<h:
        if not visited[nz][ny][nx]:
          visited[nz][ny][nx] = 1
          if graph[nz][ny][nx] == 0:
            graph[nz][ny][nx] = graph[select[0]][select[1]][select[2]] + 1
            queue.append([nz,ny,nx])
  else:
    try:
      return graph[select[0]][select[1]][select[2]]
    except:
      return 0
def check_complete():
  for i in range(h):
    for j in range(n):
      for k in range(m):
        if visited[i][j][k] == 0:
          return False
  else:
    return True

max_ = bfs() - 1
if check_complete():
  print(max_)
else:
  print("-1")