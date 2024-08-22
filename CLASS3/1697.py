from collections import deque

N, M = map(int, input().split())

queue = deque([N])

time = [0] * 100001
max_ = 100000

while queue:
  now = queue.popleft()
  if now == M:
    print(time[now])
    break
  for i in (now-1, now+1, now*2):
    if 0<=i<=max_ and not time[i]:
      queue.append(i)
      time[i] = time[now] + 1