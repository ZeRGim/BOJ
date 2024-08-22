N, r, c = map(int, input().split())
res = 0
while N > 0:
  twon = 2**(N-1)
  square = [0,0]
  square[1] = r // twon
  r = r % twon
  square[0] = c // twon
  c = c % twon
  
  if square == [0,0]:
    pass
  elif square == [0,1]:
    res += (twon**2) * 2
  elif square == [1,1]:
    res += (twon**2) * 3
  elif square == [1,0]:
    res += (twon**2) * 1
  N -= 1
print(res)