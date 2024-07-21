a,b,c,d,e,f = map(int,input().split())
if e != 0 and b != 0:
    x=[a*e,d*b]
    y=[b*e,e*b]
    p=[c*e,f*b]
    resx=(p[0]-p[1])//(x[0]-x[1])
    resy=(c-a*resx)//b
elif e == 0:
    resx=f//d
    resy=(c-a*resx)//b
else:
    resx = c//a
    resy = (f-d*resx)//e

print(resx,resy)