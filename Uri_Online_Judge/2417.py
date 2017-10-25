cv,ce,cs,fv,fe,fs = input().split()

cv = int(cv)*3
fv = int(fv)*3
ce = int(ce)
fe = int(fe)
cs = int(cs)
fs = int(fs)

if cv+ce > fv+fe:
    print("C")
elif  cv+ce<fv+fe:
    print("F")
else:
    if cs > fs:
        print("C")
    elif cs<fs:
        print("F")
    else:
        print("=")
