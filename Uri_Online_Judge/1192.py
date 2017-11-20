casos = int(input())

for i in range(casos):
    frase = input().strip()
    if int(frase[0]) == int(frase[2]):
        print(int(frase[0])*int(frase[2]))
    elif frase[1].isupper() == True:
        print(int(frase[2])-int(frase[0]))
    else:
        print(int(frase[0])+int(frase[2]))
