casos = int(input())
bom = 0
mal = 0
todos = []
for i in range(casos):
    valor, crianca = input().split()
    todos.append(crianca)
    if valor == "+":
        bom += 1
    else:
        mal += 1
todos.sort()
for j in todos:
    print(j)
print("Se comportaram: " + str(bom) + " | Nao se comportaram: " + str(mal))
