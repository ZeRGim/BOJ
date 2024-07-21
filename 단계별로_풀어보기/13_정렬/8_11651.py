def merge_sort(arr,q):
  def sort(low, high):
    if high - low < 2:
      return
    mid = (low + high) // 2
    sort(low, mid)
    sort(mid, high)
    merge(low, mid, high)

  def merge(low, mid, high):
    temp = []
    l, h = low, mid
    if q == "x":
      xory=0
    elif q == "y":
      xory=1
    while l < mid and h < high:
      if arr[l][xory] < arr[h][xory]:
        temp.append(arr[l])
        l += 1
      else:
        temp.append(arr[h])
        h += 1

    while l < mid:
      temp.append(arr[l])
      l += 1
    while h < high:
      temp.append(arr[h])
      h += 1

    for i in range(low, high):
      arr[i] = temp[i - low]

  return sort(0, len(arr))

def xsort(point:list):
  cnt=0
  dic={0:0}
  Li=[]
  cnt2=0
  Li2=[]
  for i in range(len(point)):
    Li2.append(point[i][0])
  for i in range(len(point)):
    if i == 0:
      dic[cnt] += 1
    else:
      if point[i][1] == point[i-1][1]:
        dic[cnt] += 1
      else:
        cnt += 1
        try:
          dic[cnt] += 1
        except:
          dic[cnt] = 1
  print(dic.values())
  for i in list(dic.values()):
    Li.append([])
    for j in range(i):
      Li[cnt2].append(Li2.pop(0))
    cnt2 += 1
  for i in Li:
    i.sort()
  for i in range(len(Li)-1):
    Li[0].extend(Li[i+1])
  for i in range(len(point)):
    point[i][0] = Li[0][i]
  return point
def main():
  N = int(input())
  point = []
  for i in range(N):
    point.append(list(map(int, input().split())))
  merge_sort(point, 'y')
  point = xsort(point)
  for i in point:
    print(i[0], i[1])

main()