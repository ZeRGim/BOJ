H,M=map(int, input().split())

if M >= 45:
    print("%d %d"%(H,M-45))
else:
    if H == 0:
        print("23 %d"%(M+15))
    else:
        print("%d %d"%(H-1,M+15))