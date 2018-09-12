num = int(input())
pil = []
[pil.append(x) for x in range(1,num+1)]
ret = []
while(len(pil) > 1):
    ret.append(pil[0])
    pil.pop(0)
    pil.insert(len(pil),pil[0])
    pil.pop(0)

for i in range(len(ret)):
    if i < len(ret)-1:
        print(ret[i],end=" ")
    else:
        print(ret[i])
print(str(pil[0]))
