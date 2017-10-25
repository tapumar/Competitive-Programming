l1 = ["`","1","2","3","4","5","6","7","8","9","0","-","="]
l2 = ["Q","W","E","R","T","Y","U","I","O","P"]
l3 = ["A","S","D","F","G","H","J","K","L",";","'"]
l4 = ["Z","X","C","V","B","N","M",",",".","/"]

while(True):
    try:
        frase = input()
        nova = ""
        for j in frase:
            if j in l1:
                aux = l1[(l1.index(j))-1]
            elif j in l2:
                aux = l2[(l2.index(j))-1]
            elif j in l3:
                aux = l3[(l3.index(j))-1]
            elif j in l4:
                aux = l4[(l4.index(j))-1]
            elif ord(j) == 91:
                aux = "P"
            elif ord(j) == 93:
                aux = chr(91)
            elif ord(j) == 92:
                aux = chr(93)
            else:
                aux = j
            nova += aux
        
        print(nova)
        
    except EOFError:
        break
