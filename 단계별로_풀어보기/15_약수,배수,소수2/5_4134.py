import sys

def solving(x: int):
  if x == 0 or x == 1:
    return 2
  while True:
    if check(x):
      return x
    x += 1
def check(x: int):
  for i in range(2,int(x**0.5)+1):
    if x % i == 0:
      return False
  return True

def main():
  T = int(input())
  for i in range(T):
    ans = solving(int(sys.stdin.readline()))
    print(ans)

main()