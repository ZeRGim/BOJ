# import sys
# N = int(input())
# Li=[]
# for i in range(N):
#   Li.append(int(sys.stdin.readline()))
# Li.sort()
# for i in Li:
#   print(i)
# 메모리 초과
import sys

N = int(input())
arr = {}
for i in range(N):
  temp = int(sys.stdin.readline())
  if temp in arr.keys():
    arr[temp] += 1
  else:
    arr[temp] = 1
key = list(arr.keys())
key.sort()
for i in key:
  for j in range(arr[i]):
    print(i)