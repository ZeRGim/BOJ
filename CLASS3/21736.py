# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10000)

# N, M = map(int, input().split())
# board = []
# for _ in range(N):
#   board.append(list(input().strip()))
# visited = [[0]*M for _ in range(N)]
# friend = 0
# doyeon = []
# for i in range(N):
#   if doyeon:
#     break
#   for j in range(M):
#     if board[i][j] == "I":
#       doyeon = [j,i]
#       break

# def dfs(x,y):
#   global friend
#   dx = [0,0,1,-1]
#   dy = [1,-1,0,0]
#   visited[y][x] = 1
#   for i in range(4):
#     nx = x+dx[i]
#     ny = y+dy[i]
#     if 0<=nx<M and 0<=ny<N:
#       if board[ny][nx] != "X" and visited[ny][nx] == 0:
#         visited[ny][nx] = 1
#         if board[ny][nx] == "P":
#           friend += 1
#         dfs(nx,ny)

# dfs(doyeon[0],doyeon[1])
# if friend == 0:
#   print("TT")
# else: print(friend)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input().strip()))
visited = [[0]*M for _ in range(N)]
friend = 0
doyeon = []
for i in range(N):
    if doyeon:
        break
    for j in range(M):
        if board[i][j] == "I":
            doyeon = [j,i]
            break

def dfs_non_recursive(start_x, start_y):
    global friend
    stack = [(start_x, start_y)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while stack:
        x, y = stack.pop()
        if visited[y][x]:
            continue
        visited[y][x] = 1
        if board[y][x] == "P":
            friend += 1
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and board[ny][nx] != "X":
                stack.append((nx, ny))

dfs_non_recursive(doyeon[0], doyeon[1])

if friend == 0:
    print("TT")
else:
    print(friend)