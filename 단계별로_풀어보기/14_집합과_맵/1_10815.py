def inputing():
  N = int(input())
  sang=list(map(int, input().split()))
  M = int(input())
  card=list(map(int, input().split()))
  return sang, card

def main():
  sang, card = inputing()
  temp = set(sang)
  res = []
  for i in card:
    temp.add(i)
    if len(temp) == len(sang):
      res.append("1")
    else:
      res.append("0")
      temp.remove(i)
  print(*res)
    
main()

# in으로 찾는것이 for문으로 전부 핥는것과 진배없다. 반복문안에 if in 을 넣으면
#시간 복잡도가 n^2이 되어 다른 방법이 없는지 고민할 것.