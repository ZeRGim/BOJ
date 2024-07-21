import sys
N = int(input())
Li=[]
for i in range(N):
  Li.append(int(sys.stdin.readline()))
Li.sort()
for i in Li:
  print(i)