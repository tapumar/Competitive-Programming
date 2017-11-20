num = int(input())
for i in range(num):
    palavra = input().strip()
    tam = len(palavra)
    if tam == 5:
        print("3")
    else:
        if (palavra[0] == "t" and palavra[1] == "w") or (palavra[0] == "t" and palavra[2] == "o") or (palavra[1] == "w" and palavra[2] == "o") :
            print("2")
        else:
            print("1")
