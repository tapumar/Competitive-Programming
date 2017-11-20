while(True):
    a,d = input().split(' ')
    if a== "0" and d == "0":
        break
    a= int(a)
    d = int(d)
    ataque = list(map(int,input().split()))
    defesa = list(map(int,input().split()))
    ataque.sort()
    defesa.sort()
    if ataque[0] < defesa[1]:
        print("Y")
    else:
        print("N")
