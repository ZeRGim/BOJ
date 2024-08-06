import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
K = int(input())
computers = {i:False for i in range(1,N+1)}
computers[1] = True
lines = [[] for i in range(N+1)]
for _ in range(K):
  a, b = map(int, input().split())
  lines[a].append(b)
  lines[b].append(a)
queue = deque([1])
while queue:
  node = queue.popleft()
  for i in lines[node]:
    computers[node] = True
    if not computers[i]:
      queue.append(i)
    

cnt = 0
for i in list(computers.values()):
  if i:
    cnt += 1
print(cnt - 1)