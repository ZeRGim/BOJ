import sys
input = sys.stdin.readline

class Heap(object):
  
  def __init__(self):
    self.heap = []
    self.heap.append(None)
  
  def check_swap_up(self,idx):
    if idx <= 1:
      return False
    
    parent_idx = idx // 2
    if abs(self.heap[idx]) <= abs(self.heap[parent_idx]):
      if abs(self.heap[idx]) == abs(self.heap[parent_idx]):
        if self.heap[idx] < self.heap[parent_idx]:
          return True
        else:
          return False
      else:
        return True
    else:
      return False
  
  def heap_add(self,x: int):
    self.heap.append(x)
    idx = len(self.heap) - 1
    
    while self.check_swap_up(idx):
      parent_idx = idx // 2
      self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
      idx = parent_idx
  
  def check_swap_down(self, idx: int):
    left_idx = idx * 2
    right_idx = idx * 2 + 1
    
    if left_idx > len(self.heap) - 1:
      return False
    elif right_idx > len(self.heap) - 1:
      if abs(self.heap[left_idx]) >= abs(self.heap[idx]):
        if abs(self.heap[left_idx]) == abs(self.heap[idx]):
          if self.heap[left_idx] < self.heap[idx]:
            self.flag = 1
            return True
          else:
            return False
      else:
        self.flag = 1
        return True
    else:
      if abs(self.heap[left_idx]) < abs(self.heap[right_idx]):
        if abs(self.heap[left_idx]) >= abs(self.heap[idx]):
          if abs(self.heap[left_idx]) == abs(self.heap[idx]):
            if self.heap[left_idx] < self.heap[idx]:
              self.flag = 1
              return True
            else:
              return False
        else:
          self.flag = 1
          return True
      else:
        if abs(self.heap[left_idx]) == abs(self.heap[right_idx]):
          if self.heap[left_idx] <= self.heap[right_idx]:
            if abs(self.heap[left_idx]) >= abs(self.heap[idx]):
              if abs(self.heap[left_idx]) == abs(self.heap[idx]):
                if self.heap[left_idx] < self.heap[idx]:
                  self.flag = 1
                  return True
                else:
                  return False
            else:
              self.flag = 1
              return True
          else:
            if abs(self.heap[right_idx]) >= abs(self.heap[idx]):
              if abs(self.heap[right_idx]) == abs(self.heap[idx]):
                if self.heap[right_idx] < self.heap[idx]:
                  self.flag = 2
                  return True
                else:
                  return False
            else:
              self.flag = 2
              return True
        else:
          if abs(self.heap[right_idx]) >= abs(self.heap[idx]):
            if abs(self.heap[right_idx]) == abs(self.heap[idx]):
              if self.heap[right_idx] < self.heap[idx]:
                self.flag = 2
                return True
              else:
                return False
          else:
            self.flag = 2
            return True
        
  def heappop(self):
    if len(self.heap) <= 1:
      print("0")
      return
    
    absmin = self.heap[1]
    self.heap[1] = self.heap[-1]
    del self.heap[-1]
    idx = 1
    
    self.flag = 0
    while self.check_swap_down(idx):
      left_idx = idx * 2
      right_idx = idx * 2 + 1
      
      if self.flag == 1:
        self.heap[left_idx], self.heap[idx] = self.heap[idx], self.heap[left_idx]
        idx = left_idx
      elif self.flag == 2:
        self.heap[right_idx], self.heap[idx] = self.heap[idx], self.heap[right_idx]
        idx = right_idx
    print(absmin)
    return

n = int(input())

myheap = Heap()

for _ in range(n):
  querie = int(input())
  if querie == 0:
    myheap.heappop()
  else:
    myheap.heap_add(querie)