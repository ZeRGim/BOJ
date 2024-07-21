num=[666]
N=int(input())
cnt = 666
while len(num)<=N:
    cnt += 1
    if '666' in str(cnt):
        num.append(cnt)
print(num[N-1])