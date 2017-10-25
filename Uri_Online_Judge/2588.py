alfa = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

while(True):
    try:
        palavra = input().strip()
        impar = 0
        for i in alfa:
            aux = palavra.count(i)
            if aux%2 != 0:
                impar += 1
        if impar == 0:
            print("0")
        else:   
            print(impar-1)

    except EOFError:
        break
