import sys
input = sys.stdin.readline

N = int(input())

meeting_time = []
for i in range(N):
  a, b = map(int, input().split())
  meeting_time.append([b,a])
meeting_time.sort()
now = meeting_time.pop(0)
cnt = 1
for i in meeting_time:
  if i[1] >= now[0]:
    cnt += 1
    now = [i[0], i[1]]
print(cnt)