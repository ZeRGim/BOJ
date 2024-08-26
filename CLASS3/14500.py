import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n, m = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
max_ = 0
def dfs(x,y,temp,cnt):
  global max_
  if cnt == 4:
    max_ = max(temp, max_)
    return
  dx = [0,0,-1,1]
  dy = [-1,1,0,0]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<m and 0<=ny<n and not visited[ny][nx]:
      visited[ny][nx] = 1
      dfs(nx,ny,temp+board[ny][nx], cnt+1)
      visited[ny][nx] = 0

def uwu(x,y):
  global max_
  up = y-1
  down = y+1
  left = x-1
  right = x+1
  #ㅜ operate
  if left < 0 or right >= m or down >= n:
    pass
  else:
    max_ = max(max_, (board[y][x]+board[y][left]+board[y][right]+board[down][x]))
  #ㅏ operate
  if right >= m or down >= n or up < 0:
    pass
  else:
    max_ = max(max_, (board[y][x]+board[up][x]+board[y][right]+board[down][x]))
  #ㅗ operate
  if left < 0 or right >= m or up < 0:
    pass
  else:
    max_ = max(max_, (board[y][x]+board[y][left]+board[y][right]+board[up][x]))
  #ㅓ operate
  if left < 0 or up < 0 or down >= n:
    pass
  else:
    max_ = max(max_, (board[y][x]+board[y][left]+board[up][x]+board[down][x]))

for i in range(n):
  for j in range(m):
    visited[i][j] = 1
    dfs(j, i, board[i][j], 1)
    visited[i][j] = 0
    
    uwu(j,i)

print(max_)