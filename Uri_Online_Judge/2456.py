orden = input().split()
orden = [int(x) for x in orden]
nova = sorted(orden)
novaI = nova[::-1]

if orden == nova:
    print("C")
elif orden == novaI:
    print("D")
else:
    print("N")
