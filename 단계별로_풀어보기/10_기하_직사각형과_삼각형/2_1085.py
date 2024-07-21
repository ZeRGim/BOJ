x,y,w,h = map(int, input().split())

candi=[w-x,h-y,x,y]
print(min(candi))