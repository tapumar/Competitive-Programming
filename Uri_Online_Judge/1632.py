esp = ["a","e","i","o","s"]
casos = int(input())
for k in range(casos):
    senha = input().strip()
    vari = 1
    for i in senha:
        if i.lower() in esp:
            vari *= 3
        else:
            vari *= 2
    print(vari)
