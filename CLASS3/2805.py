# N, M = map(int, input().split())
# trees = list(map(int, input().split()))
# tallest = max(trees)
# point = tallest//2
# last = [0,tallest]
# while True:
#   total = 0
#   for i in trees:
#     if i-point > 0:
#       total += i-point
#   if total > M:
#     last[0] = point
#     point = (point+last[1])//2
#   elif total < M:
#     last[1] = point
#     point = (point+last[0])//2
#   else:
#     print(point)
#     break
N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2
    total = sum(tree - mid if tree > mid else 0 for tree in trees)
    
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)