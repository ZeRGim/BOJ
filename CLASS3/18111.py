import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
blocks = {}
for _ in range(N):
  temp = list(map(int, input().split()))
  for i in temp:
    try:
      blocks[i] += 1
    except:
      blocks[i] = 1
bk = list(blocks.keys())
res = []
for i in range(257):
  temp = []
  hap = 0
  need = 0
  have = B
  for j in bk:
    temp.append((i-j)*blocks[j])
  for k in temp:
    if k > 0:
      hap += k
      need += k
    else:
      hap -= 2*k
      have -= k
  if need <= have:
    res.append([hap,i])
res.sort()
temp = [i for i in res if i[0] == res[0][0]]
temp.sort()
print(temp[len(temp)-1][0], temp[len(temp)-1][1])