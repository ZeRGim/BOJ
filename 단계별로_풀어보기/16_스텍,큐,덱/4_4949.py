import sys

while True:
  temp = sys.stdin.readline().rstrip("\n")
  if temp[0] == ".": break
  temp = list(temp)
  temp.reverse()
  a = 0
  b = 0
  res = True
  stack = []
  for i in temp:
    if i == ")":
      a += 1
      stack.append(")")
    elif i == "]":
      b += 1
      stack.append("]")
    elif i == "(":
      a -= 1
      if len(stack) == 0:
        res = False
        break
      if stack.pop() != ")":
        res = False
        break
    elif i == "[":
      b -= 1
      if len(stack) == 0:
        res = False
        break
      if stack.pop() != "]":
        res = False
        break
    if a < 0 or b < 0:
      res = False
      break
  if a != 0 or b != 0:
    res = False
  if res:
    print("yes")
  else:
    print("no")