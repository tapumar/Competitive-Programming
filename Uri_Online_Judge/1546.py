feed = {1:"Rolien", 2:"Naej", 3:"Elehcim", 4:"Odranoel"}

casos = int(input())
for i in range(casos):
    num = int(input())
    for j in range(num):
        feedback = int(input())
        print(feed[feedback])
