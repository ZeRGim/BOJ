import sys

def solving(x: int, y: int):
  Li = set()
  for i in range(x,y+1):
    if i == 1:
      Li.add(2)
      continue
    if check(i):
      Li.add(i)
  return Li

def check(x: int):
  for i in range(2,int(x**0.5)+1):
    if x % i == 0:
      return False
  return True

def main():
  A,B = map(int, input().split())
  ans = solving(A, B)
  for i in ans:
    print(i)

main()