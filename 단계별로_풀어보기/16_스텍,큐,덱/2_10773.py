import sys

N = int(input())
Li = []
for _ in range(N):
  temp = int(sys.stdin.readline())
  if temp == 0:
    Li.pop()
  else: Li.append(temp)

print(sum(Li))