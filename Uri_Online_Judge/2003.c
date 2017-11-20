#include <stdio.h>
 
int main() {
 
 int hora,min;
 
 while(scanf("%d:%d", &hora,&min) != EOF){
 
    if(hora<7){
         printf("Atraso maximo: 0\n");
     }
     else if(hora>=8){
         if(hora==9){
             printf("Atraso maximo: 120\n");
         }
         else{
             printf("Atraso maximo: %d\n", (min+60));
        }
    }
     else if(hora==7){
         if(min==0){
             printf("Atraso maximo: 0\n"); 
         }
         else{
              printf("Atraso maximo: %d\n", min);
         }
     }
 }
 
    return 0;
}
