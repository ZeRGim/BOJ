import sys
input = sys.stdin.readline
from collections import deque
N = int(input())

board = []
for _ in range(N):
  temp = list(input().strip())
  board.append([int(i) for i in temp])
visited = [[0]*N for i in range(N)]

def bfs(x,y):
  if not board[y][x] or visited[y][x]:
    return 0
  queue = deque([[x,y]])
  dx = [0,0,1,-1]
  dy = [1,-1,0,0]
  cnt = 1
  while queue:
    now = queue.popleft()
    visited[now[1]][now[0]] = 1
    for i in range(4):
      nx = now[0] + dx[i]
      ny = now[1] + dy[i]
      if 0<=nx<N and 0<=ny<N:
        if board[ny][nx] and not visited[ny][nx]:
          visited[ny][nx] = 1
          queue.append([nx,ny])
          cnt += 1
  return cnt
danzi = []
for i in range(N):
  for j in range(N):
    temp = bfs(j,i)
    if temp:
      danzi.append(temp)
print(len(danzi))
danzi.sort()
for i in danzi:
  print(i)