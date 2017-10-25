while(True):
    n,m = input().split()
    if n == "0" and m == "0":
        break
    if len(n) >= len(m):
        num1 = n[::-1]
        num2 = m[::-1]
    else:
        num2 = n[::-1]
        num1 = m[::-1]
    soma = 0
    sobra = "0"
    for i in range(len(num1)):
        if i < len(num2): 
            sobra = str((int(num2[i]) + int(num1[i])) + int(sobra))
        else:
           sobra =  str(int(sobra) + int(num1[i]))
        if int(sobra) >= 10:
            sobra = sobra[0]
        else:
            sobra = "0"
            
        if sobra != "0":
            soma += 1
    if soma == 0:
        print("No carry operation.")
    elif soma == 1:
        print("1 carry operation.")
    else:
        print(str(soma)  + " carry operations.")
