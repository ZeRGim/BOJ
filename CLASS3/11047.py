import sys
input = sys.stdin.readline

N, K = map(int, input().split())
worth = []
for _ in range(N):
  worth.append(int(input()))
worth.reverse()
cnt = 0
for i in worth:
  temp = K // i
  cnt += temp
  K -= temp * i

print(cnt)