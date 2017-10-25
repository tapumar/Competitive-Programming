num = int(input())

teste = {1:"sheldon",0:"rajesh"}
for i in range(num):
    
    jogo = input().split()

    if "spock" in jogo:
        
        if "tesoura" in jogo or "pedra" in jogo:
            print(teste[jogo.index("spock")])
            
        elif "papel" in jogo:
            print(teste[jogo.index("papel")])
            
        elif "lagarto" in jogo:
            print(teste[jogo.index("lagarto")])
            
        else:
            print("empate")
            
    elif "tesoura" in jogo:
        
        if "pedra" in jogo:
            print(teste[jogo.index("pedra")])
            
        elif "papel" in jogo or "lagarto" in jogo:
            print(teste[jogo.index("tesoura")])
            
        else:
            print("empate")
        
    elif "lagarto" in jogo:
        
        if "pedra" in jogo:
            print(teste[jogo.index("pedra")])
            
        elif "papel" in jogo:
            print(teste[jogo.index("lagarto")])
            
        else:
            print("empate")
            
    elif "pedra" in jogo:
        
        if "papel" in jogo:
            print(teste[jogo.index("papel")])
        else:
            print("empate")
    else:
        print("empate")
