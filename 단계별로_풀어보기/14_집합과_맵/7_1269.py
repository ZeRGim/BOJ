def inputing():
  N, M = map(int, input().split())
  A = set(map(int, input().split()))
  B = set(map(int, input().split()))
  
  return A, B

def main():
  A, B = inputing()
  C = A - B
  D = B - A
  F = C | D
  print(len(F))

main()