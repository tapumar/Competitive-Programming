bin = input()
n = bin.replace("0","")
if len(n)%2 == 0:
    print(bin + "0")
else:
    print(bin + "1")
