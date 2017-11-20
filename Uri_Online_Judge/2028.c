#include <stdio.h>
 
int main() {
 
 int caso, cont,i,j, CasoNum=1 ;
 
    while(scanf("%d", &caso) != EOF){
        cont=1;
        for(i=1;i<=caso;i++){
            cont=cont+i;
        }
        if(cont==1){
            printf("Caso %d: %d numero\n",CasoNum, cont);
        }
        else{
            printf("Caso %d: %d numeros\n",CasoNum,cont);
        }
        
        CasoNum++;
        i=1;
        j=1;
        printf("0");
        while(j<=caso){
            i=1;
            while(i<=j){
                printf(" %d", j); 
                i++;
            }

            j++;
        }
        printf("\n\n");
    }
    return 0;
}
