base = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V"]

while(True):
    num = int(input())
    n = num
    numero = ""
    while(True):
        if n < 32:
            numero += base[n]
            break
        else:
            resto = n%32
            n = int(n/32)
            numero += base[resto]
    print(numero[::-1])
    if num == 0:
        break
