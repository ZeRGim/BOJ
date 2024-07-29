import sys

def inputing():
  N = int(input())
  Li = []
  for i in range(N):
    Li.append(int(sys.stdin.readline()))
  return Li

def yaksu(x: int):
  res = []
  for i in range(1, int(x**0.5)+2):
    if x % i == 0:
      res.append(i)
  for i in range(len(res)):
    res.append(x//res[i])
  return res

def cal(gong: set, Li: list):
  res = []
  for i in range(len(Li) - 1):
    res.append(Li[i+1] - Li[i])
  res.sort()
  arr = []
  for i in gong:
    for j in res:
      if j % i != 0:
        break
    else:
      arr.append(i)
  ans = max(arr)
  cnt = 0
  for i in res:
    cnt += i // ans
  return cnt - len(res)

def gong(Li:list):
  res = []
  for i in range(len(Li) - 1):
    res.append(Li[i+1] - Li[i])
  res.sort()
  A = res.pop(0)
  B = res.pop(0)
  Ayak = set(yaksu(A))
  Byak = set(yaksu(B))
  gong = Ayak & Byak
  return gong
  
def main():
  Li = inputing()
  gongyaksu = gong(Li)
  ans = cal(gongyaksu, Li)
  print(ans)

main()