line = input().strip()
marc = 0
codigo = {}
nova = ""
for i in line:
    codigo[marc+97] = i
    marc += 1
frase = input().strip()
for j in frase:
    nova = nova + codigo[ord(j)]
print(nova)
