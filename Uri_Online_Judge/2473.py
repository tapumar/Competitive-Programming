aposta = input().split()
sorteio = input().split()
mark = 0
for i in range(len(aposta)):
    if aposta[i] in sorteio:
        mark += 1
if mark < 3:
    print("azar")
elif mark == 3:
    print("terno")
elif mark == 4:
    print("quadra")
elif mark == 5:
    print("quina")
else:
    print("sena")
