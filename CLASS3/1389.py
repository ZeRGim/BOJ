import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[0]*(N+1) for i in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  board[a][b] = board[b][a] = 1

bacon = [[0]*(N+1) for i in range(N+1)]

def bfs(x,y):
  visited = [0]*(N+1)
  queue = deque([x])
  visited[x] = 1
  road = {}
  while queue:
    temp = queue.popleft()
    if temp == y:
      break
    for i in range(1,N+1):
      if board[temp][i] == 1 and visited[i] == 0:
        queue.append(i)
        visited[i] = 1
        road[i] = temp
  cnt = 0
  while True:
    if temp == x:
      break
    cnt += 1
    temp = road[temp]
  bacon[x][y] = bacon[y][x] = cnt

for i in range(1,N+1):
  for j in range(1,N+1):
    if bacon[i][j] == 0:
      bfs(i,j)
bacon_sum = []
for i in range(1,N+1):
  bacon_sum.append(sum(bacon[i]))
bacon_min = min(bacon_sum)
print(bacon_sum.index(bacon_min)+1)