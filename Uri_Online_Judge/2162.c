#include <stdio.h>
 
int main() {
 
    int n,i, anterior,med,aux,aux1,cont=1;
    
    scanf("%d", &n);
    
    scanf("%d", &med);
    anterior =med;
    aux=0;
    aux1=0;
    for (i=1;i<n;i++){
        scanf("%d",&med);
        if(med>anterior && aux==0){
            aux=1;
            aux1=0;
            cont++;
        }
        else if(med< anterior && aux1==0){
            aux1=1;
            aux=0;
            cont++;
        }
        anterior = med;
    }
    if(cont==n){
        printf("1\n");
    }
    else{
        printf("0\n");
    }
    return 0;
}
