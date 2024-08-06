import sys
input = sys.stdin.readline

N, M = map(int, input().split())
site_password = {}
for _ in range(N):
  s, p = input().split()
  p = p.strip()
  site_password[s] = p
for _ in range(M):
  temp = input().strip()
  print(site_password[temp])