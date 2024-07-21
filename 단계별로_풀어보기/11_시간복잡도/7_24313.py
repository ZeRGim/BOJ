a1,a0 = map(int, input().split())
c=int(input())
n0=int(input())

def check(a1,a0,c,n0):
    for i in range(n0,101):
        if a1*i+a0 > c*i:
            return False
    return True

def main():
    if check(a1,a0,c,n0):
        print("1")
    else: print("0")
        
main()