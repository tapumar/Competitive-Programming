while(True):
    pessoas = input().strip()
    if pessoas == "0":
        break
    pessoas = int(pessoas)
    salto = 1
    while(True):
        pont = 0
        circulo = [x for x in range(1,pessoas+1)]
        while(len(circulo) > 1):
            while(pont >= len(circulo)):
                pont = pont - len(circulo)
            circulo.pop(pont)
            pont -= 1
            pont += salto
        salto += 1
        if circulo[0] == 13:
            break
    print(salto-1)
