import sys

def inputing():
  N = int(input())
  Li = []
  for i in range(N):
    Li.append(list(sys.stdin.readline().split()))
  for i in Li:
    i[0] = int(i[0])
    i[1].strip()
  return Li

def sorting(Li: list):
  tempLi = []
  for i in range(200):
    tempLi.append([])
  for i in Li:
    tempLi[i[0]-1].append(i[1])
  return tempLi
def main():
  Li = inputing()
  res = sorting(Li)
  for i in range(len(res)):
    if res[i]:
      for j in res[i]:
        print(i+1, j)

main()