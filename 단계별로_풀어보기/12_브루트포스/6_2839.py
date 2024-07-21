N = int(input())
cnt=-1
mok=N//5
for i in range(mok+1):
    Q = N - 5*(mok-i)
    if Q % 3 == 0:
        cnt = (mok-i) + (Q//3)
        break
print(cnt)