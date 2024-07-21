def cal(x,i,j):
    return x*(B**(j-i))

N, B=input().split()
B=int(B)
ori=0

for i in range(len(N)):
    if B == 10:
        ori=N
        break
    try:
        k=int(N[i])
        a=cal(k,i+1,len(N))
        ori += a        
    except:
        tempn=ord(N[i])-55
        a=cal(tempn,i+1,len(N))
        ori += a
print(ori)