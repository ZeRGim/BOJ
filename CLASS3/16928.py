import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())

board = [i for i in range(101)]
visited = [0]*101
for i in range(n+m):
  a,b = map(int,input().split())
  board[a] = b

def bfs():
  queue = deque([[1,0]])
  
  while queue:
    select = queue.popleft()
    now, attempt = select
    visited[now] = 1
    if now == 100:
      return attempt
    for i in range(1,7):
      if now+i <= 100 and not visited[now+i]:
        visited[now+i] = 1
        queue.append([board[now+i], attempt+1])

print(bfs())