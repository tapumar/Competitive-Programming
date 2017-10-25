while(True):
    try:
        n = int(input())
        soma = 0
        while(n>1):
            
            soma += 1
            n = n/2
            
        print(soma)
        
    except EOFError:
        break
