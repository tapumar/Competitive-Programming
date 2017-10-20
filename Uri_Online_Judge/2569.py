calc = input().split()

n1 = calc[0].replace("7","0")
n2 = calc[2].replace("7","0")
if calc[1] == "+":
  res = int(n1) + int(n2)
else:
  res = int(n1) * int(n2)
res = int(str(res).replace("7","0"))
print(res)

