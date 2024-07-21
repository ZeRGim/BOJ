import sys
def inputing():
  N, M = map(int, input().split())
  myword = []
  checkword = []
  for i in range(N):
    myword.append(sys.stdin.readline())
  for i in range(M):
    checkword.append(sys.stdin.readline())
  return myword, checkword
def main():
  myword, checkword = inputing()
  Set=set(myword)
  cnt=0
  for i in checkword:
    Set.add(i)
    if len(myword) == len(Set):
      cnt += 1
    else:
      Set.remove(i)
  print(cnt)

main()