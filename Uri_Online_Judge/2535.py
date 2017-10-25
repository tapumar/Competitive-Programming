while(True):
    try:
        qnt = int(input())
        total = 0
        for i in range(qnt): 
            especie = input().strip()
            raca = input().strip()
            nome = input().split()
            aux = input()
            if especie == "cachorro" and len(nome)>1:
                for j in nome:
                    if j[0] == raca[0]:
                        total += 1
                        break
        print(total)
        
    except EOFError:
        break
                
