import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
board = [list(input().strip()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
def bfs_origin(x,y):
  if visited[y][x]:
    return 0
  cnt = 1
  queue = deque([[x,y]])
  while queue:
    select = queue.popleft()
    visited[select[1]][select[0]] = 1
    RGB = board[select[1]][select[0]]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for _ in range(4):
      nx = select[0] + dx[_]
      ny = select[1] + dy[_]
      if 0<=nx<n and 0<=ny<n:
        if not visited[ny][nx] and board[ny][nx] == RGB:
          visited[ny][nx] = 1
          queue.append([nx,ny])
          cnt += 1
  return cnt

ter = []
for i in range(n):
  for j in range(n):
    temp = bfs_origin(j,i)
    if temp:
      ter.append(temp)
print(len(ter), end=" ")

visited = [[0]*n for _ in range(n)]
def bfs_reprise(x,y):
  if visited[y][x]:
    return 0
  cnt = 1
  queue = deque([[x,y]])
  while queue:
    select = queue.popleft()
    visited[select[1]][select[0]] = 1
    RGB = board[select[1]][select[0]]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for _ in range(4):
      nx = select[0] + dx[_]
      ny = select[1] + dy[_]
      if 0<=nx<n and 0<=ny<n:
        if not visited[ny][nx]:
          if RGB == "B":
            if board[ny][nx] == RGB:
              visited[ny][nx] = 1
              queue.append([nx,ny])
              cnt += 1
          else:
            if board[ny][nx] != "B":
              visited[ny][nx] = 1
              queue.append([nx,ny])
              cnt += 1
  return cnt

ter = []
for i in range(n):
  for j in range(n):
    temp = bfs_reprise(j,i)
    if temp:
      ter.append(temp)
print(len(ter))