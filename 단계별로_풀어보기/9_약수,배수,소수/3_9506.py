import sys

while True:
    a=int(sys.stdin.readline())
    if a==-1:
        break
    Li=[]
    for i in range(a):
        if a%(i+1)==0:
            Li.append(i+1)
    try:
        Li.pop()
    except:
        pass
    if sum(Li)==a:
        print(f"{a} = ", end="")
        for i in range(len(Li)):
            if i==len(Li)-1:
                print(Li[i])
            else: print(f"{Li[i]} + ", end="")
    else: print(f"{a} is NOT perfect.")