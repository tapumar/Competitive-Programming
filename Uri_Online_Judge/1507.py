casos = int(input())
for i in range(casos):
    seq = input().strip()
    q = int(input())
    for j in range(q):
        r = input().strip()
        pont = 0
        for k in seq:
            if k == r[pont]:
                pont += 1
            if pont == len(r):
                break
        if pont == len(r):
            print("Yes")
        else:
            print("No")
