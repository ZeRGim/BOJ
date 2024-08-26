import sys
input = sys.stdin.readline
import heapq

def isEmpty(nums):
    for item in nums:
        if item[1] > 0:
            return False
    return True

t = int(input())
for _ in range(t):
  minheap = []
  maxheap = []
  nums = {}
  k = int(input())
  for i in range(k):
    querie, num = input().split()
    num = int(num)
    
    if querie == "I":
      if num in nums:
        nums[num] += 1
      else:
        nums[num] = 1
        heapq.heappush(minheap, num)
        heapq.heappush(maxheap, -num)
    else:
      if not isEmpty(nums.items()):
        if num == 1:
          while -maxheap[0] not in nums or nums[-maxheap[0]] < 1:
            temp = -heapq.heappop(maxheap)
            if temp in nums:
              del(nums[temp])
          nums[-maxheap[0]] -= 1
        
        else:
          while minheap[0] not in nums or nums[minheap[0]] < 1:
            temp = heapq.heappop(minheap)
            if temp in nums:
              del(nums[temp])
          nums[minheap[0]] -= 1

  if isEmpty(nums.items()):
    print("EMPTY")
  else:
    while -maxheap[0] not in nums or nums[-maxheap[0]] < 1:
      heapq.heappop(maxheap)
    while minheap[0] not in nums or nums[minheap[0]] < 1:
      heapq.heappop(minheap)
    print(-maxheap[0], minheap[0])