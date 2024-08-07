import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  clothes = {}
  for i in range(n):
    a, b = input().strip().split()
    try:
      clothes[b] += 1
    except KeyError:
      clothes[b] = 1
  days = 1
  for i in clothes.keys():
    days *= (clothes[i]+1)
  print(days-1)