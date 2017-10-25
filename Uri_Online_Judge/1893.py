antes,depois = input().split()
antes = int(antes)
depois = int(depois)

if (depois <=96 and depois >= 3) and antes > depois:
    print("minguante")
elif depois >= 0 and depois < 3:
    print("nova")
elif depois >= 3 and depois <= 96:
    print("crescente")
else:
    print("cheia")
