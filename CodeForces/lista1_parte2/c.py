n = int(input())
erros0 = input().split()
erros1 = input().split()
copy = erros1[:]
erros2 = input().split()
res = list(set(erros0).difference(erros1))
if not res:
    for i in erros0:
        if not i in erros1 or erros1.remove(i):
            print(i)
            break
else:
    print(res[0])
res = list(set(erros1).difference(erros2))
if not res:
    for i in copy:
        if not i in erros2 or erros2.remove(i):
            print(i)
            break
else:
    print(res[0])
