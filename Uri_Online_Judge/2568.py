d,i,x,f = input().split()
d = int(d)
i = int(i)
x = int(x)
f = int(f)
if d%2 != 0:
  if (d+f)%2 == 0:
    print(i+x)
  else:
    print(i)
else:
  if (d+f)%2 == 0:
    print(i)
  else:
    print(i-x)
  