#2 3 5 9
#+1 +2 +4 +8

N=int(input())
line=2
a=1
for i in range(N):
    line += a
    a=a*2
print(line**2)