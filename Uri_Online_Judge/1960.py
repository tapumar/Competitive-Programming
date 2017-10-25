romano = ["I","V","X"]
romano10 = ["X","L","C"]
romano100 = ["C","D","M"]

n = input().strip()
tam = len(n)
n = n[::-1]
numero = ""
for i in range(tam):
    if i == 0:
        novo = romano
    elif i == 1:
        novo = romano10
    else:
        novo = romano100
    if n[i] == "1":
       numero += novo[0]
    elif n[i] == "2":
        numero += novo[0] + novo[0]
    elif n[i] == "3":
        numero += novo[0] + novo[0]+novo[0]
    elif n[i] == "4":
        numero += novo[1] + novo[0]
    elif n[i] == "5":
        numero += novo[1]
    elif n[i] == "6":
        numero += novo[0] + novo[1]
    elif n[i] == "7":
        numero += novo[0] + novo[0] + novo[1]
    elif n[i] == "8":
        numero += novo[0] + novo[0]+novo[0] + novo[1]
    elif n[i] == "9":
        numero += novo[2] + novo[0]
print(numero[::-1])
