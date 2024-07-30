from collections import deque
import sys
def main():
  stack = deque([])
  def command(x: str, y: int|None = None):
    if x == "push":
      stack.append(y)
    elif x == "pop":
      if stack:
        print(stack.popleft())
      else: print("-1")
    elif x == "size":
      print(len(stack))
    elif x == "empty":
      if stack: print("0")
      else: print("1")
    elif x == "front":
      if stack: print(stack[0])
      else: print("-1")
    elif x == "back":
      if stack: print(stack[len(stack)-1])
      else: print("-1")
  N = int(input())
  for _ in range(N):
    request = list(sys.stdin.readline().split())
    if len(request) == 1:
      command(request[0])
    else:
      command(x=request[0], y=int(request[1]))

main()