while(True):
  p,s = input().split()
  if p == "0" and s == "0":
    break
  p = int(p)
  s = int(s)
  t1,t2,t3 = input().split()
  t1 = int(t1)
  t2 = int(t2)
  t3 = int(t3)
  n = int(input())
  jog = [0 for i in range(p)]
  arm = []
  vez = 0
  mark = 0
  for i in range(n):
    if vez > p-1:
      vez = 0
    while(vez in arm):
      arm.remove(vez)
      vez += 1
      if vez > p-1:
        vez = 0
    d1,d2 = input().split()
    jog[vez] += (int(d1) + int(d2))
    if jog[vez] == t1 or jog[vez] == t2 or jog[vez] == t3:
      arm.append(vez)
    if jog[vez] > s and mark == 0:
      vencedor = vez+1
      mark = 1
    vez += 1
  print(vencedor)
