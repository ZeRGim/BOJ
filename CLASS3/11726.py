import sys
input = sys.stdin.readline

n = int(input())
a = n // 4
b = n % 4
a = 5**a
if b == 3:
  a *= 10
elif b == 2:
  a *= 5
elif b == 1:
  a *= 2
print(a)