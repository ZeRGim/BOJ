#Q=25, D=10, N=5, P=1
import sys

T=int(input())

for i in range(T):
    money=int(sys.stdin.readline())
    Q=money//25
    money = money%25
    D=money//10
    money = money%10
    N=money//5
    money = money%5
    P=money
    
    print(Q,D,N,P)
        