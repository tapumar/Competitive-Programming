while(True):
    try:
        frase = input()
        novaFrase = ""
        for i in frase:
            n = ord(i)
            if (n >=65 and n<=90) or (n>=97 and n<=122):
                n=n+13
                
                if n>122:
                    n = n-122+96
                    
                elif n>90 and i.isupper()==True:
                    n = n-90+64
               
            novaFrase = novaFrase+chr(n)
    
        print(novaFrase)  
        
    except EOFError:
        break
