import sys
from collections import deque
def solving():
  count, index = map(int, sys.stdin.readline().split())
  Queue = deque(map(int, sys.stdin.readline().split()))
  cnt = 0
  while True:
    
    if index == 0 and Queue[0] == max(Queue):
      return cnt + 1
    elif index == 0 and Queue[0] != max(Queue):
      index += len(Queue)
      
    if Queue[0] != max(Queue):
      Queue.append(Queue.popleft())
    else:
      Queue.popleft()
      cnt += 1
    
    index -= 1
  

def main():
  T = int(input())
  for _ in range(T):
    print(solving())

main()