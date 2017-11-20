n = int(input())
sa=0
bl=0
at=0
sa1=0
bl1=0
at1=0
for i in range(n):
    nome = input()
    s,b,a = input().split(" ")
    s1,b1,a1 = input().split(" ")
    s= int(s)
    b=int(b)
    a=int(a)
    s1= int(s1)
    b1=int(b1)
    a1=int(a1)
    sa = sa+s
    bl = bl+b
    at = at+a
    sa1=sa1+s1
    bl1=bl1+b1
    at1=at1+a1
print("Pontos de Saque: " + '%.2f'%((sa1*100)/sa) + " %.")
print("Pontos de Bloqueio: " + '%.2f'%((bl1*100)/bl) + " %.")
print("Pontos de Ataque: " + '%.2f'%((at1*100)/at) + " %.")
    
