#include  <stdio.h>

int main(void)
{
    int casos;
    int x,y,soma,i;
    
    scanf("%d", &casos);
    
    for(i = 0;i<casos;i++){
        scanf("%d %d", &x, &y);
        soma = x+y;
        if(soma == 0){
             printf("PROXYCITY\n");
        }
        else if(soma == 1){
             printf("P.Y.N.G.\n");
        }
        else if(soma == 2){
             printf("DNSUEY!\n");
        }
        else if(soma == 3){
             printf("SERVERS\n");
        }
        else if(soma == 4){
             printf("HOST!\n");
        }
        else if(soma == 5){
             printf("CRIPTONIZE\n");
        }
        else if(soma == 6){
             printf("OFFLINE DAY\n");
        }
        else if(soma == 7){
             printf("SALT\n");
        }
        else if(soma == 8){
             printf("ANSWER!\n");
        }
        else if(soma == 9){
             printf("RAR?\n");
        }
        else{
             printf("WIFI ANTENNAS\n");
        }
        
        
    }
    
        
        
    return 0;
}
