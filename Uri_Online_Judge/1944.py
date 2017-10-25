num = int(input())
pil = []
soma = 0
for i in range(num):
    letras = input().split()
    if len(pil) == 0: 
        pil.append(['F','A','C','E'])
    aux =  pil[len(pil)-1]
    if letras == aux[::-1]:
        pil.pop(len(pil)-1)
        soma += 1
    else: 
        pil.append(letras)
        
print(soma)
