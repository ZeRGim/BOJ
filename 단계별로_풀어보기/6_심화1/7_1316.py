def check(word):
    for j in alpa:
        temp=[]
        if word.count(j) > 1:
            for k in range(word.count(j)):
                temp.append(word.find(j))
                word=word.replace(j," ",1)
            for q in range(len(temp)):
                try:
                    if temp[q+1]-temp[q] != 1:
                        return 0
                    
                except:
                    continue


N=int(input())
alpa=[]
cnt=0
for i in range(65,91):
    alpa.append(chr(i).lower())
for i in range(N):
    word=input()
    a=check(word)
    if a == None:
        cnt += 1
print(cnt)