import sys

def solving(x: int):
  Li = [i for i in range(x+1,2*x+1)]
  sqrt = int(x**0.5)+1
  for i in range(2,sqrt+3):
    for j in range(2,Li[len(Li)-1]):
      try:
        Li.remove(i*j)
      except: continue
  print(Li)
  return len(Li)

def main():
  x = 1
  while x != 0:
    x = int(sys.stdin.readline())
    if x == 0:
      break
    ans = solving(x)
    print(ans)

main()