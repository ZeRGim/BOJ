# N = int(input())
# fruits = list(input().split())
# candi = []
# for i in range(N,0,-1):
#   for j in range(0,i):
#     temp = fruits[j:i]
#     if len(set(temp)) <=2:
#       candi.append(i-j)
# print(max(candi))
N = int(input())
fruits = input().split()

max_length = 0
window_start = 0
fruit_count = {}

for window_end in range(N):
    current_fruit = fruits[window_end]
    
    if current_fruit in fruit_count:
        fruit_count[current_fruit] += 1
    else:
        fruit_count[current_fruit] = 1
    
    while len(fruit_count) > 2:
        start_fruit = fruits[window_start]
        fruit_count[start_fruit] -= 1
        if fruit_count[start_fruit] == 0:
            del fruit_count[start_fruit]
        window_start += 1
    
    max_length = max(max_length, window_end - window_start + 1)

print(max_length)