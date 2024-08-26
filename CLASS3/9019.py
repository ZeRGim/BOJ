import sys
from collections import deque

def bfs(A, B):
  queue = deque([A])
  visited = [0]*10000
  dp = ['']*10000
  visited[A] = 1

  while queue:
    select = queue.popleft()

    if dp[B] != '':
      return dp[B]

    # D operation
    D = (2*select) % 10000
    if not visited[D]:
      visited[D] = 1
      queue.append(D)
      dp[D] = dp[select] + 'D'

    # S operation
    S = (select - 1) % 10000
    if not visited[S]:
      visited[S] = 1
      queue.append(S)
      dp[S] = dp[select] + 'S'

    # L operation
    L = (select % 1000) * 10 + select // 1000
    if not visited[L]:
      visited[L] = 1
      queue.append(L)
      dp[L] = dp[select] + 'L'

    # R operation
    R = (select // 10) + (select % 10) * 1000
    if not visited[R]:
      visited[R] = 1
      queue.append(R)
      dp[R] = dp[select] + 'R'
  return dp[B]

input = sys.stdin.readline
t = int(input().strip())

for _ in range(t):
    A, B = map(int, input().strip().split())
    print(bfs(A, B))