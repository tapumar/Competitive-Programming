xm,ym,xr,yr = input().split()
xm = int(xm)
ym = int(ym)
xr = int(xr)
yr = int(yr)

dist = abs(xr-xm) + abs(yr-ym)
print(dist)