h,m=map(int,input().split())
t=int(input())
th=t//60
tm=t-(th*60)
rh=h+th
rm=m+tm
if rm >= 60:
    rh+=1
    rm-=60
if rh >= 24:
    print("%d %d"%(rh-24,rm))
else:
    print("%d %d"%(rh, rm))