N=int(input())
M=2*N-1
Q=((M-1)//2)
for i in range(Q):
    print(" "*(Q-i)+"*"*(1+2*i))
print("*"*(2*Q+1))
for i in range(Q-1,-1,-1):
    print(" "*(Q-i)+"*"*(1+2*i))