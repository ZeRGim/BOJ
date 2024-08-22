import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())

board = []
for _ in range(N):
  temp = list(input().strip())
  board.append([int(i) for i in temp])
visited = [[0]*M for i in range(N)]
def bfs():
  queue = deque([[0,0]])
  dx = [0,0,1,-1]
  dy = [1,-1,0,0]
  while queue:
    now = queue.popleft()
    visited[now[1]][now[0]] = 1
    for i in range(4):
      nx = now[0] + dx[i]
      ny = now[1] + dy[i]
      if 0<=nx<M and 0<=ny<N:
        if board[ny][nx] and not visited[ny][nx]:
          board[ny][nx] = board[now[1]][now[0]] + 1
          visited[ny][nx] = 1
          queue.append([nx,ny])
bfs()
print(board[N-1][M-1])