while(True):
    try:
        frase = input().split()
        somaPal = 0
        somaLet = 0
        for i in frase:
            if "1" not in i and "2" not in i and "3" not in i and "4" not in i and "5" not in i and "6" not in i and "7" not in i and "8" not in i and "9" not in i and "0" not in i:
                if i.count(".") < 1:
                    somaPal += 1
                    somaLet += len(i)
                elif i.count(".") == 1 and i[-1] == "." and len(i) > 1:
                    somaPal += 1
                    somaLet += (len(i)-1)
        if somaPal == 0:
            cal = 0
        else:
            cal = int(somaLet/somaPal)
        if cal <= 3:
            print("250")
        elif cal >= 6:
            print("1000")
        else:
            print("500")
                                      
    except EOFError:
        break
