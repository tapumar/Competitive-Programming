while(True):
    try:
        
        numAtributos = int(input())
        NumMar,NumLeo = input().split()
        Marcos = []
        Leo = []
        for i in range(int(NumMar)):
            Marcos.append(input().split())
        for j in range(int(NumLeo)):
            Leo.append(input().split())
        Cm,Cl = input().split()
        Atributo = int(input())
        
        Vm = int(Marcos[int(Cm)-1][Atributo-1])
        Vl = int(Leo[int(Cl)-1][Atributo-1])
        if Vm > Vl:
            print("Marcos")
        elif Vl > Vm:
            print("Leonardo")
        else:
            print("Empate")
    except EOFError:
        break
