n,t,l = input().split()
n = int(n)
t = int(t)
l = int(l)
pontAlice = 0
pontBob = 0
for i in range(n-1):
    topo = int(input())
    aux = abs(topo-t)
    if aux <= l:
        t = topo
        if i%2 == 0:
            pontAlice += aux
        else:
            pontBob += aux
    
print(pontAlice,pontBob)
        
