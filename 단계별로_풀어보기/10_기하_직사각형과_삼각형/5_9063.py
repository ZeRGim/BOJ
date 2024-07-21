N = int(input())
x=[]
y=[]
if N == 1:
  print(0)
else:
  for i in range(N):
    temp_x, temp_y = map(int, input().split())
    x.append(temp_x)
    y.append(temp_y)
  res = (max(x) - min(x)) * (max(y) - min(y))
  print(res)