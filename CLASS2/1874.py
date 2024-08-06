import sys
input = sys.stdin.readline

N = int(input()) #N개
Li = [i for i in range(1,N+1)] #1부터 N까지의 리스트
want = []
for _ in range(N):
  want.append(int(input())) #요구되는 수열

stack = [] #임시적으로 쌓일 스택
made = [] #내가 만들어낸 수열
res = [] #푸시 팝 기록
cnt = 0 #want를 해치지않으면서 다음으로 넘어가기 위한 수단
for i in Li:
  res.append("+")
  stack.append(i)
  while True:
    if stack:
      if stack[len(stack)-1] == want[cnt]:
        made.append(stack.pop())
        res.append("-")
        cnt += 1
      else: break
    else:
      break
for _ in range(len(stack)):
  made.append(stack.pop())
  res.append("-")
if want == made:
  for i in res:
    print(i)
else:
  print("NO")