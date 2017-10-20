n1,d1,v1 = input().split()
n2,d2,v2 = input().split()

t1 = int(d1)/int(v1)
t2 = int(d2)/int(v2)
if t1 < t2:
  print(n1)
else:
  print(n2)