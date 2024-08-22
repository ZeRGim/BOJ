import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())

board_origin = []
blue = 0
white = 0
for _ in range(N):
  board_origin.append(list(map(int, input().split())))

def check(board):
  global blue
  global white
  a = 0
  b = 0
  for i in range(len(board)):
    for j in range(len(board)):
      a += board[j][i]
      b += 1
  if a == b:
    blue += 1
    return
  elif a == 0:
    white += 1
    return
  else:
    board_copy = []
    for i in range(0,len(board)//2):
      board_copy.append(board[i][0:len(board)//2])
    check(board_copy)
    board_copy = []
    for i in range(0,len(board)//2):
      board_copy.append(board[i][len(board)//2:len(board)])
    check(board_copy)
    board_copy = []
    for i in range(len(board)//2,len(board)):
      board_copy.append(board[i][len(board)//2:len(board)])
    check(board_copy)
    board_copy = []
    for i in range(len(board)//2,len(board)):
      board_copy.append(board[i][0:len(board)//2])
    check(board_copy)

check(board_origin)
print(white)
print(blue)