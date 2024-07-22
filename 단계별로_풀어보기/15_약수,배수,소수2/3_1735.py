def inputing():
  A,B = map(int, input().split())
  C,D = map(int, input().split())
  return A,B,C,D

def yaksu_cal(x: int):
  yaksu = []
  for i in range(1,int(x**0.5)+2):
    if x % i == 0:
      yaksu.append(i)
  for i in range(len(yaksu)):
    yaksu.append(x//yaksu[i])
  return yaksu

def solving(A:int, B:int):
  Ayaksu = set(yaksu_cal(A))
  Byaksu = set(yaksu_cal(B))
  gongyak = max(Ayaksu & Byaksu)
  return A*B//gongyak

def soinsu(x: int):
  temp = x
  dic = {}
  while temp != 1:
    for i in range(2,int(x**0.5)+3):
      if temp % i == 0:
        try:
          dic[i] += 1
        except:
          dic[i] = 1
        temp = temp // i
        break
    else:
      break
  return dic

def main():
  A,B,C,D = inputing()
  mo = solving(B,D)
  A = A*(mo//B)
  C = C*(mo//D)
  ja = A+C

  moso = soinsu(mo)
  jaso = soinsu(ja)
  
  if moso and jaso:
    for i in list(jaso.keys()):
      if moso[i] >= jaso[i]:
        mo = mo // (i**jaso[i])
        ja = ja // (i**jaso[i])
      else:
        mo = mo // (i**moso[i])
        ja = ja // (i**moso[i])
  
  print(ja, mo)
  
main()