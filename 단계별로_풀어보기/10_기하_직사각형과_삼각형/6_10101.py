angle=[]
for i in range(3):
  angle.append(int(input()))
if angle[0] == angle[1] and angle[1] == angle[2]:
  print("Equilateral")
elif sum(angle) == 180:
  if angle[0] == angle[1] or angle[1] == angle[2] or angle[0] == angle[2]:
    print("Isosceles")
  else: print("Scalene")
else: print("Error")