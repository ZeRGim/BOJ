word=input()
croa=['c=','c-','dz=','d-','lj','nj','s=','z=']
alpa=[]
cnt=0
for i in range(65,91):
    alpa.append(chr(i).lower())
for i in croa:
    if i in word:
        if word.count(i)>1:
            for k in range(word.count(i)):
                        cnt += 1
                        word=word.replace(i," ",1)
                        
        else:
            cnt += 1
            word=word.replace(i," ")
            
for i in alpa:
    if i in word:
        if word.count(i)>1:
            for k in range(word.count(i)):
                        cnt += 1
                        word=word.replace(i," ",1)
        else:
            cnt += 1
            word=word.replace(i," ")
print(cnt)

