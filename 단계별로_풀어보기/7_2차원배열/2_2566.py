Li=[]
for i in range(9):
    temp=list(map(int, input().split()))
    Li.append(temp)
maxi=0
hang=1
yeol=1
for i in range(9):
    for j in range(9):
        if maxi<Li[i][j]:
            maxi=Li[i][j]
            hang=i+1
            yeol=j+1
print(maxi)
print(hang, yeol)