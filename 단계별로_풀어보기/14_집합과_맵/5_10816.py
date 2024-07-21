def inputing():
  N = int(input())
  having = list(input().split())
  M = int(input())
  card = list(input().split())
  
  return having, card

def main():
  having, card= inputing()
  cnt = {}
  for i in having:
    try:
      cnt[i] += 1
    except:
      cnt[i] = 1
  
  for i in card:
    try:
      print(cnt[i], end=" ")
    except:
      print("0", end=" ")
    
main()