word=input()
word=word.upper()
cntli=[]
maxi=0
for i in range(65,92):
    res=word.count(chr(i))
    cntli.append(res)
for i in cntli:
    if maxi<i:
        maxi=i
if cntli.count(maxi) is not 1:
    print("?")
else:
    a=cntli.index(maxi)
    print(chr(a+65))
