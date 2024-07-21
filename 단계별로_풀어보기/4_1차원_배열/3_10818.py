import sys
N=int(input())

Li=list(sys.stdin.readline().split())
for q in range(len(Li)):
    Li[q]=int(Li[q])
for i in range(len(Li)):
    try:
        if Li[i] > Li[i+1]:
            Li[i], Li[i+1]=Li[i+1], Li[i]
    except:
        break
for j in range(-1,-N,-1):
    try:
        if Li[j] < Li[j-1]:
            Li[j-1], Li[j] = Li[j], Li[j-1]
    except:
        break
mini=Li[0]
maxi=Li[N-1]
print(mini, maxi)