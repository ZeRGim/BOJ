import sys

def inputing():
  N, M = map(int, input().split())
  listen = {}
  see = []
  for i in range(N):
    listen[(sys.stdin.readline().strip())] = 0
  for i in range(M):
    see.append(sys.stdin.readline().strip())
  
  return listen, see

def main():
  listen, see = inputing()
  res = []
  for i in see:
    try:
      listen[i] += 1
      res.append(i)
    except:
      pass
  res.sort()
  print(len(res))
  for i in res:
    print(i)

main()