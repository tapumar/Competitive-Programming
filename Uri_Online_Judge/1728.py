while(True):
    eq = input().strip()
    pri, rest = eq.split("+")
    seg, rest = rest.split("=")
    pri = pri[::-1]
    seg = seg[::-1]
    rest = rest[::-1]
    if int(pri)+int(seg) == int(rest):
        print("True")
    else:
        print("False")
    if seg == "0" and pri == "0" and rest == "0":
        break
