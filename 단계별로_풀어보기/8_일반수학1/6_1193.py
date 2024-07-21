x=int(input())
i=1
while x>0:
    x -= i
    i+=1

if (i-1)%2 == 0:
    print(f"{i-1+x}/{1-x}")
else:
    print(f"{1-x}/{i-1+x}")