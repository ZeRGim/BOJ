while True:
  triangle=list(map(int, input().split()))
  if sum(triangle) == 0:
    break
  if sum(triangle) - 2*max(triangle) > 0:
    if triangle[0] == triangle[1] and triangle[1] == triangle[2]:
      print("Equilateral")
    elif triangle[0] == triangle[1] or triangle[1] == triangle[2] or triangle[0] == triangle[2]:
      print("Isosceles")
    else:
      print("Scalene")
  else: print("Invalid")