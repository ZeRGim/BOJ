import sys

def inputing():
  N = int(input())
  log = {}
  for i in range(N):
    temp = list(sys.stdin.readline().split())
    log[temp[0]] = temp[1]
  return log

def main():
  log = inputing()
  res = []
  for i in list(log.keys()):
    if log[i] == "enter":
      res.append(i)
  res.sort()
  res.reverse()
  for i in res:
    print(i)

main()