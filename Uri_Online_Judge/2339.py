comp, folhas,cada = input().split()
comp= int(comp)
folhas = int(folhas)
cada = int(cada)

if folhas >= (comp*cada):
    print("S")
else:
    print("N")
