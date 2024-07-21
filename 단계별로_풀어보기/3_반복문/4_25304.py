X=int(input())
N=int(input())
hap=0
for i in range(N):
    price, cnt=map(int, input().split())
    hap += price*cnt
if X==hap:
    print("Yes")
else:
    print("No")