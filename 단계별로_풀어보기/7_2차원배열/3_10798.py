Li=[]
maxlen=0
maxind=0
for i in range(5):
    a=input()
    Li.append(a)
    if maxlen < len(a):
        maxlen = len(a)
        maxind = i
for i in range(maxlen):
    for j in range(5):
        try:
            print(Li[j][i], end = "")
        except:
            continue