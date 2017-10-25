while(True):
    try:
        nova = ""
        frase = input().strip()
        nova = frase
        for i in range(len(frase)):
            
            for k in range(i):
                print(" ",end="")
            for j in range(len(nova)):
                if j< len(nova)-1:
                    print(nova[j],end=' ')
                else:
                    print(nova[j])
        
            nova = nova[:-1]
            
        print()
    except EOFError:
        break
