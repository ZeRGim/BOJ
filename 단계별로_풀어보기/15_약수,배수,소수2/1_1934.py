import sys

def inputing(N):
  Li = []
  for i in range(N):
    Li.append(list(map(int, sys.stdin.readline().split())))
  return Li

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
  N = int(input())
  Li = inputing(N)
  for i in Li:
    print(solving(i[0], i[1]))
    
main()