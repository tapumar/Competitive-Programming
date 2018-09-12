carros, est = input().split()
carros = int(carros)
est = int(est)
saida = []
check = True
c, s = input().split()
saida.append(int(s))
for i in range(carros-1):
    c, s = input().split()
    saida.append(int(s))
    est -= 1
    t = len(saida)
    while (True):
        if len(saida) > 1 and saida[-2] <= int(c):
            del saida[-2]
            est += 1
        else:
            break
    if est < 0:
        check = False

if check == True:
    s_aux = saida[-1]
    while(True):
        if len(saida) > 1:
            s_aux = saida[-1]
            if saida[-1] <= saida[-2]:
                del saida[-1]
            else:
                check = False
                break
        else:
            if s_aux > saida[-1]:
                check = False
            break
if check:
    print("Sim")
else:
    print("Nao")
close
