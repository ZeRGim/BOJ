import sys
input = sys.stdin.readline

  
N, K = map(int, input().split())
Li = []
for _ in range(N):
  Li.append(int(input()))
res = 0
  
def binary(low:int, high:int):
  global Li
  global res
  if high < low:
    return
  cnt = 0
  mid = (low + high + 1) // 2
  for i in Li:
    cnt += i //mid
  if cnt >= K:
    res = mid
    binary(mid+1, high)
  else:
    binary(low, mid-1)
  
binary(0,max(Li))
print(res)

