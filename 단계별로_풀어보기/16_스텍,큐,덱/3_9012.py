import sys
T = int(input())

for _ in range(T):
  A = sys.stdin.readline().strip()
  cnt = len(A)//2+1
  for i in range(cnt):
    A = A.replace("()", "")
  if A: print("NO")
  else: print("YES")