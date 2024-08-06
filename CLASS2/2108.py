import sys

def sansul(dic: dict):
  res = 0
  for x, y in dic.items():
    res += x*y
  res = round (res / sum(dic.values()) + 0.0000000001)
  return res
def middle(Li: list):
  return Li[(len(Li)+1)//2-1]
  
def frequent(dic: dict):
  Li = []
  dimax = max(dic.values())
  for i in dic.keys() :
    if dic[i] == dimax:
      Li.append(i)
  Li.sort()
  try: return Li[1]
  except: return Li[0]
def rangee(dic:dict):
  return max(dic.keys()) - min(dic.keys())

def main():
  N = int(input())
  dic = {}
  Li = []
  
  for _ in range(N):
    temp = int(sys.stdin.readline())
    try:
      dic[temp] += 1
    except KeyError:
      dic[temp] = 1
    Li.append(temp)
  Li.sort()
  print(sansul(dic))
  print(middle(Li))
  print(frequent(dic))
  print(rangee(dic))

main()