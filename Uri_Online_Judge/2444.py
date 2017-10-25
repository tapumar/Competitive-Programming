volume, t = input().split()

volume = int(volume)

trocas = input().split()

for i in trocas:
    i = int(i)
    volume += i
    if volume > 100:
        volume = 100
    elif volume < 0:
        volume = 0
print(volume)
    
