M = int(input())
N = int(input())
def check(n):
    if n == 1:
            return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def main():
    Li = []
    for i in range(M,N+1):
        if check(i):
            Li.append(i)
    if len(Li) == 0:
        print('-1')
    else:
        Li.sort()
        print(sum(Li))
        print(Li[0])
        
main()