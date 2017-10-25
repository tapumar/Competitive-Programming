pal = input()
frase = input().split()
nova = ""
mark = 0
for i in frase:
    if mark == 1:
        nova += " "
    if i[0] == "U" and i[1] == "R" and len(i)==3:
        nova += "URI"
    elif i[0] == "O" and i[1] == "B" and len(i)==3:
        nova += "OBI"
    else:
        nova += i
    mark = 1
print(nova)
