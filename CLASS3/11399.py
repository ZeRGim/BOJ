N = int(input())
Li = list(map(int, input().split()))
Li.sort()
cnt = 0
for i in range(len(Li)):
  cnt += sum(Li[:i+1])
print(cnt)