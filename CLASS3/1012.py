import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
T = int(input())

def dfs(x,y):
  dx = [0,0,-1,1]
  dy = [1,-1,0,0]
  for i in range(4):
    new_x = x+dx[i]
    new_y = y+dy[i]
    if 0<=new_x<M and 0<=new_y<N:
      if maps[new_y][new_x] == 1:
        maps[new_y][new_x] = 0
        dfs(new_x,new_y)

for _ in range(T):
  M, N, K = map(int,input().split())
  maps = [[0 for i in range(M)] for j in range(N)]
  for i in range(K):
    x, y = map(int, input().split())
    maps[y][x] = 1
  cnt = 0
  for i in range(N):
    for j in range(M):
      if maps[i][j] == 1:
        cnt += 1
        dfs(j,i)
  print(cnt)