while(True):
    
    buraco,vel = input().split()
    if buraco == "0" and vel == "0":
        break
    bola = 0
    buraco = int(buraco)
    vel = int(vel)
    v = 0
    velaux = vel
    aux = vel
    mark = 0
    while(velaux > 0):
        v = velaux
        bola = 0
        aux = velaux
        while(aux > 0 and bola < buraco):
            bola += aux
            if bola == buraco:
                mark = 1
                break
            v -= 1
            if v == 0:
                aux -= 1
                v = aux
        if mark == 1:
            break
        velaux -= 1
    if mark == 1:
        print("possivel")
    else:
        print("impossivel")
