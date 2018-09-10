a,b = input().split()
t = a + b
t = int(t)
r = t ** (1/2)
r = str(r).split(".")
if r[1] == "0":
    print("Sim")
else:
    print("Nao")
