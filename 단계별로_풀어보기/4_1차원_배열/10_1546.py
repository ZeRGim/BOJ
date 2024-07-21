N=int(input())
Li=[]
Li=input().split()
maxi=0
temp=[]
for i in Li:
    if maxi<int(i):
        maxi=int(i)
for i in Li:
    temp.append(int(i)/maxi*100)
hap=0
for i in temp:
    hap += i
avg=hap/N
print(avg)