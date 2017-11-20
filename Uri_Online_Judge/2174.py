casos = int(input())

todos = {}
for i in range(casos):
    pokemon = input().strip()
    try:
      teste = todos[pokemon]
    except:
      todos[pokemon] = pokemon
print("Falta(m) "+str(151-len(todos))+" pomekon(s).")
