prova = int(input())

notas = {0:"A",1:"B",2:"C",3:"D",4:"E"}
while(True):
    if prova == 0:
        break
        
    for i in range(prova):
        questao = input().split()
        questao = [int(x) for x in questao]
        questaoMarcada = [y for y in questao if y<=127]
        questaoBranca = [y for y in questao if y>127]
        
        if len(questaoMarcada) == 1:
            print(notas[questao.index(questaoMarcada[0])])
        else:
            print("*")
    
    prova = int(input())
