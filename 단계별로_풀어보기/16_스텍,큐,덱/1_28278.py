import sys

def inputing():
  temp = sys.stdin.readline().strip()
  if temp[0] == '1':
    return temp.split()
  else: return temp

def main():
  N = int(input())
  Li = []
  def command(x: str, y: str | None = None):
    if x == "1":
      Li.append(int(y))
    elif x == "2":
      if len(Li) > 0:
        print(Li.pop())
      else:
        print("-1")
    elif x == "3":
      print(len(Li))
    elif x == "4":
      if len(Li) == 0:
        print("1")
      else: print("0")
    elif x == "5":
      if len(Li) > 0:
        print(Li[len(Li)-1])
      else:
        print("-1")
    elif x == "6":
      print(Li)
  for i in range(N):
    inp = list(inputing())
    if len(inp) == 1:
      command(inp[0])
    else: command(inp[0], inp[1])

main()