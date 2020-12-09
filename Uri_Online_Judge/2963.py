votos = int(input())
carlos = int(input())
eleito = True
for voto in range(votos-1):
    adv = int(input())
    if adv > carlos:
        eleito = False

if eleito:
    print("S")
else:
    print("N")
