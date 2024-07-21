M = int(input())
while True:
    for i in range(2,M+1):
        if M % i == 0:
            print(i)
            M = M // i
            break
    if M == 1:
        break