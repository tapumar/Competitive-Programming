l,n = input().split()

irregular ={}
for i in range(int(l)):
      a,b = input().split()
      irregular[a] = b
for j in range(int(n)):
    comida = input().strip()
    try:
        plural = irregular[comida]
        print(plural)
    except:
        if comida[len(comida)-1] == "y" and comida[len(comida)-2] != "a"and comida[len(comida)-2] != "e" and comida[len(comida)-2] != "i" and comida[len(comida)-2] != "o" and comida[len(comida)-2] != "u":
            comida = comida.replace("y","")
            comida = comida + "ies"
        elif comida[len(comida)-1] == "o" or comida[len(comida)-1] == "s" or (comida[len(comida)-1] == "h" and comida[len(comida)-2] == "c") or (comida[len(comida)-1] == "h" and comida[len(comida)-2] == "s") or comida[len(comida)-1] == "x":
            comida = comida + "es"
        else:
            comida = comida + "s"
        print(comida)
