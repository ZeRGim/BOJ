import sys

def inputing():
  N, M = map(int, input().split())
  Li={}
  Question = []
  for i in range(N):
    Li[(sys.stdin.readline().rstrip())] = i+1
  for i in range(M):
    Question.append(str(sys.stdin.readline().rstrip()))
  return Li, Question

def main():
  Li, Question = inputing()
  temp = list(Li.keys())
  for i in range(len(Question)):
    if Question[i].isdigit():
      print(temp[int(Question[i])-1])
    else:
      print(Li[Question[i]])

main()