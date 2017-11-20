#include <stdio.h>
 
int main() {
    
    int lista, cont2=0,cont3=0,cont4=0,cont5=0,i,num;
 
    scanf("%d", &lista);
    for(i=0;i<lista;i++){
        scanf("%d", &num);
        
        if(num%2==0){
            cont2++;
        }
        if(num%3==0){
            cont3++;
        }
        if(num%4==0){
            cont4++;
        }
        if(num%5==0){
            cont5++;
        }
    }
    printf("%d Multiplo(s) de 2\n",cont2);
    printf("%d Multiplo(s) de 3\n",cont3);
    printf("%d Multiplo(s) de 4\n",cont4);
    printf("%d Multiplo(s) de 5\n",cont5);
    
return 0;
}
