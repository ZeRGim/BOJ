triangle = list(map(int, input().split()))
while True:
  if sum(triangle) - 2*max(triangle) > 0:
    break
  triangle[triangle.index(max(triangle))] -= 1
print(sum(triangle))