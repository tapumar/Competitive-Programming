n = input()
votos = input().split()
votos = [int(x) for x in votos]
total = sum(i for i in votos)
primeiro = max(votos)
votos.remove(primeiro)
segundo = max(votos)
if (primeiro >= total*0.45) or (primeiro>=0.40 and primeiro-segundo >= total*0.1):
    print("1")
else:
    print("2")
