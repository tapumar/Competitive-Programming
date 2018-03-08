casos = int(input())

for i in range(casos):
    flag_zero = False
    flag_inv = False
    ra = input().strip()
    if ra[0] != 'R' or ra[1] != 'A' or len(ra) != 20:
        flag_inv = True
    else:
        numero = ""
        for j in range(18):
            if ra[j+2] != "0":
                flag_zero = True
                for k in range(18-j):
                    if ra[k+j+2].isdigit():
                        numero += ra[k+j+2]
                    else:
                        flag_inv = True
                break
    if flag_inv == True or flag_zero == False:
        print("INVALID DATA")
    else:
        print(numero)
