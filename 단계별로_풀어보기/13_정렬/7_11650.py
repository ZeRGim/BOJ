# def merge_sort(arr,q):
#   def sort(low, high):
#     if high - low < 2:
#       return
#     mid = (low + high) // 2
#     sort(low, mid)
#     sort(mid, high)
#     merge(low, mid, high)

#   def merge(low, mid, high):
#     temp = []
#     l, h = low, mid
#     if q == "x":
#       xory=0
#     elif q == "y":
#       xory=1
#     while l < mid and h < high:
#       if arr[l][xory] < arr[h][xory]:
#         temp.append(arr[l])
#         l += 1
#       else:
#         temp.append(arr[h])
#         h += 1

#     while l < mid:
#       temp.append(arr[l])
#       l += 1
#     while h < high:
#       temp.append(arr[h])
#       h += 1

#     for i in range(low, high):
#       arr[i] = temp[i - low]

#   return sort(0, len(arr))

# def main():
#   N = int(input())
#   point = []
#   for i in range(N):
#     point.append(list(map(int, input().split())))
#   merge_sort(point, 'x')
#   merge_sort(point, 'y')
  
#   for i in point:
#     print(i[0], i[1])

# main()

# y정렬할때 문제생김

N = int(input())
Li=[]
for i in range(N):
  Li.append(list(map(int, input().split())))
Li.sort()
for i in Li:
  print(i[0], i[1])

#내장 sort함수가 리스트도 알아서 잘 솔트하는구나 .., 나중에 직접구현해보기.