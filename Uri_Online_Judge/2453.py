frase = input().split()
nova = ""
for i in frase:
  for j in range(len(i)):
    if j%2 != 0:
      nova += i[j]
  nova += " "
print(nova.strip())