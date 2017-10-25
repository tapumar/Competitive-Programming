n,m = input().split()

while(True):
    if n == "0" and m == "0":
        break
    n = int(n)
    m = int(m)
    soma = str(n+m)
    soma = soma.replace("0","")
    print(soma)
    n,m = input().split()
