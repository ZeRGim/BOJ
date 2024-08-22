import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  M,N,x,y = map(int, input().split())
  xc = 1
  yc = 1
  cnt = 1
  while xc != M or yc != N:
    if xc == x and yc == y:
      print(cnt)
      break
    xc += 1
    yc += 1
    if xc > M:
      xc = 1
    if yc > N:
      yc = 1
    cnt += 1
  else:
    print("-1")