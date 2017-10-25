import math

while(True):
    try:
        jogo = input().split()
        jogo = [int(x) for x in jogo]
        
        d1 = math.sqrt( math.pow( jogo[0]-jogo[2], 2 ) + math.pow( jogo[1]-jogo[3], 2) ) + ( jogo[4]*1.5 );
        d2 = jogo[5] + jogo[6];

        if( d2 >= d1 ):
            print("Y")
        else:
            print("N")

        
    except EOFError:
        break
