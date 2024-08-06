import sys
input = sys.stdin.readline

dic = {i:False for i in range(1,21)}

def command(req: str, x: int|None = None):
  global dic
  if req == "add":
    dic[x] = True
    return
  elif req == "remove":
    dic[x] = False
    return
  elif req == "check":
    if dic[x]:
      print("1")
    else:
      print("0")
    return
  elif req == "toggle":
    if dic[x]:
      dic[x] = False
    else:
      dic[x] = True
    return
  elif req == "all":
    for i in range(1,21):
      dic[i] = True
    return
  elif req == "empty":
    for i in range(1,21):
      dic[i] = False
    return

M = int(input())
for _ in range(M):
  req = list(input().split())
  if len(req) == 1:
    command(req=req[0])
  else:
    command(req=req[0], x=int(req[1]))