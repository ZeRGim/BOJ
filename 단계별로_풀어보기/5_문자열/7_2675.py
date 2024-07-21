import sys
T=int(input())

for i in range(T):
    R,S=sys.stdin.readline().split()
    R=int(R)
    for j in range(len(S)):
        print(S[j]*R, end="")
    print("")