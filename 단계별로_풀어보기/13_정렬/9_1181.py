def inputing():
  N = int(input())
  Li = []
  for i in range(N):
    Li.append(input())
  return Li

def sort_word(Li:list):
  tempLi = []
  for i in range(50):
    tempLi.append([])
  res = []
  for i in Li:
    tempLi[len(i)-1].append(i)
  for i in tempLi:
    temp = list(set(i))
    temp.sort()
    res.append(temp)
  return res

def main():
  Li = inputing()
  res = sort_word(Li)
  for i in res:
    if i:
      for j in i:
        print(j)

main()