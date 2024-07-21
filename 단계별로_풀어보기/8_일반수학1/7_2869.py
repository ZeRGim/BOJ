import math
A,B,V=map(int, input().split())

nd=V-A

q=A-B

day=nd/q
day=math.ceil(day)

print(day+1)