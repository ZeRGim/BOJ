word = input()
Set:set = set()
for i in range(1,len(word)+1):
  cnt = 0
  for j in range(len(word)-i+1):
    print(word[cnt:cnt+i])
    Set.add(word[cnt:cnt+i])
    cnt += 1

print(len(Set))