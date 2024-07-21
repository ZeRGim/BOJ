N = int(input())
Li = list(map(int, input().split()))
L2 = list(set(Li))
L2.sort()
dic = {L2[i] : i for i in range(len(L2))}
for i in Li:
  print(dic[i], end=" ")
  
#sort 했을때 index값이 결국 자신보다 작은 좌표의 개수