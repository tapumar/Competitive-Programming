while(True):
    try:
        n = int(input())
        votos = input().split()
        num = votos.count("1")
        if num >= (len(votos)*2/3):
            print("impeachment")
        else:
            print("acusacao arquivada")

    except EOFError:
        break
        
