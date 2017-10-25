casos = int(input())

for i in range(casos):
    pessoas,salto = input().split()
    pessoas = int(pessoas)
    salto = int(salto)
    circulo = [x for x in range(1,pessoas+1)]
    pont = -1
    while(len(circulo) > 1):
        pont += salto
        while(pont >= len(circulo)):
            pont = pont - len(circulo)
        circulo.pop(pont)
        pont -= 1
    print("Case "+ str(i+1)+": "+str(circulo[0]))
