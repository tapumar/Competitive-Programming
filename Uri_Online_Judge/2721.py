renas = ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen", "Rudolph"]

bolas = input().split()
index = -1
for x in bolas:
    index += int(x)
    while(index >= len(bolas)):
        index = index - len(bolas)

print(renas[index])
