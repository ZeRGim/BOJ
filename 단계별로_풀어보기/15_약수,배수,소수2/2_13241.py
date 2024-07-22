import sys

def inputing():
  A, B =map(int, sys.stdin.readline().split())
  return A,B

def yaksu_cal(x: int):
  yaksu = []
  for i in range(1,int(x**0.5)+2):
    if x % i == 0:
      yaksu.append(i)
  for i in range(len(yaksu)):
    yaksu.append(x//yaksu[i])
  return yaksu

def solving(A:int, B:int):
  Ayaksu = set(yaksu_cal(A))
  Byaksu = set(yaksu_cal(B))
  gongyak = max(Ayaksu & Byaksu)

  return A*B//gongyak

def main():
  A, B = inputing()
  print(solving(A, B))
    
main()