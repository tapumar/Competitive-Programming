def mdc(m, n):
    if m % n == 0:
        return n
    else:
        return mdc(n, m % n)
    
while(True):
    try:
        num = int(input())
        for i in range(num):
            ope = input().strip()
            if "+" in ope:
                ope = ope.split("+")
                ope1 = ope[0].split("/")
                ope2 = ope[1].split("/")
                numerador = ((int(ope1[0])*int(ope2[1]))+(int(ope2[0])*int(ope1[1])))
                denominador = (int(ope1[1])*int(ope2[1]))
                
            elif "-" in ope:
                ope = ope.split("-")
                ope1 = ope[0].split("/")
                ope2 = ope[1].split("/")
                numerador = ((int(ope1[0])*int(ope2[1]))-(int(ope2[0])*int(ope1[1])))
                denominador = (int(ope1[1])*int(ope2[1]))
                
            elif "*" in ope:
                ope = ope.split("*")
                ope1 = ope[0].split("/")
                ope2 = ope[1].split("/")
                numerador = int(ope1[0])*int(ope2[0])
                denominador = int(ope1[1])*int(ope2[1])
                
            else:
                ope = ope.split("/")
                numerador = int(ope[0])*int(ope[3])
                denominador = int(ope[2])*int(ope[1])
                

            n = mdc(numerador,denominador)
            print(str(numerador) + "/" + str(denominador) + " = " + str(int(numerador/n)) + "/" + str(int(denominador/n)))
                   
    except EOFError:
        break
