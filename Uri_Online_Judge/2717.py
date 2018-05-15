minutos = int(input())
presente1, presente2 = input().split()
presente1 = int(presente1)
presente2 = int(presente2)
if (presente1 + presente2) > minutos:
    print("Deixa para amanha!")
else:
    print("Farei hoje!")
