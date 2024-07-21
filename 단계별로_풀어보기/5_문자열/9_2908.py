A,B=input().split()

temp=A[-1:-4:-1]
A=temp
temp=B[-1:-4:-1]
B=temp
if A>B:
    print(A)
else:
    print(B)