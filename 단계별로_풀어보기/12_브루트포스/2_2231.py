N=int(input())
Li=[]
for i in range(1000000):
    if i > N:
        break
    stri=str(i)
    sum=i
    for j in range(len(stri)):
        sum += int(stri[j])
    if sum == N:
        Li.append(i)
if Li:
    print(min(Li))
else: print("0")