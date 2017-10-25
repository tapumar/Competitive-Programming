casos = int(input())
for i in range(casos):
    frase = input()
    nova = frase
    aux = 0
    nova = nova.replace("oulupukk","9")
    aux =  nova.find("9")
    while(aux >= 0):
        nova = nova[:aux-1]+"Joulupukki"+nova[aux+2:]
        aux =  nova.find("9")
        
    print(nova)
