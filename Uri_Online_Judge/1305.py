while(True):
    try:
        num = input()
        cutoff = float(input())
        num = num.split('.')
        try:
            inteiro = int(num[0])
        except ValueError:
            inteiro = 0

        fra = 0.0
        if len(num) > 1:
            fra = float('0.'+ num[1])

        if fra > cutoff:
            print(inteiro+1)
        else:
            print(inteiro)

    except EOFError:
        break
        
