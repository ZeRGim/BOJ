import sys
from collections import deque
import math

def main():
  n = int(input())
  if n == 0:
    print("0")
    return
  
  d = []
  for _ in range(n):
    d.append(int(sys.stdin.readline()))
  d.sort()
  d = deque(d)
  people = round(n * (15/100)+0.000001)
  for _ in range(people):
    d.pop()
    d.popleft()
  res = round(sum(d) / (n - people*2)+0.0000001)
  print(res)

main()