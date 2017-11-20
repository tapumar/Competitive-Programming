#include <stdio.h>
 
int main() {
    int n,f,total,i;
    char nome[20];
    
scanf("%d", &n);
while(n != 0){
    total = 0;
    for(i=0;i<n;i++){
        scanf("%d", &f);
        scanf("%[^\n]", nome);
        if(strcmp(nome, " suco de laranja") == 0)
                total = total + (120*f);
        else if(strcmp(nome, " morango fresco") == 0)
                total = total + (85*f);
        else if(strcmp(nome, " mamao") == 0)
                total = total + (85*f);
        else if(strcmp(nome, " goiaba vermelha") == 0)
                total = total + (70*f);
        else if(strcmp(nome, " manga") == 0)
                total = total + (56*f);
        else if(strcmp(nome, " laranja") == 0)
                total = total + (50*f);
        else if(strcmp(nome, " brocolis") == 0)
                total = total + (34*f);
    }
    if(total<110){
        printf("Mais %d mg\n", (110-total));
    }
    else if(total>130){
        printf("Menos %d mg\n", (total-130));
    }
    else{
        printf("%d mg\n", total); 
    }
    scanf("%d", &n);
}
 
    return 0;
}
