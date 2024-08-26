import sys
input = sys.stdin.readline
from collections import deque
T = int(input())

for _ in range(T):
  querie = input().strip()
  n = int(input())
  arr = deque(input().strip().lstrip("[").rstrip("]").split(","))
  if arr[0] == '':
    arr.pop()
  point = 0
  error = 0
  queries = len(querie)
  for i in range(queries):
    if querie[i] == "R":
      if point == 0:
        point = -1
      else:
        point = 0
    elif querie[i] == "D":
      try:
        if point == 0:
          arr.popleft()
        else:
          arr.pop()
      except:
        print("error")
        error = 1
        break
  if error:
    continue
  if len(arr) >= 1:
    print("[", end="")
    if point == 0:
      for i in range(len(arr)-1):
        print(arr[i], end=",")
      print(arr[-1], end="]\n")
    else:
      for i in range(len(arr)-1):
        print(arr[point-i], end=",")
      print(arr[0], end="]\n")
  else:
    print("[]")