#include <stdio.h>
 
int main() {
 
   int cod,al=0,gas=0,di=0;

	scanf("%d",&cod);
	while(cod<1 || cod>4){
		scanf("%d",&cod);
	}
	while(cod!=4){
		
		if(cod==1){
			al++;
		}
		else if(cod==2){
			gas++;
		}
		else if(cod==3){
			di++;
		}
		scanf("%d",&cod);
		while(cod<1 || cod>4){
			scanf("%d",&cod);
		}
	}

	printf("MUITO OBRIGADO\n");
	printf("Alcool: %d\n",al);
	printf("Gasolina: %d\n",gas);
	printf("Diesel: %d\n",di);
 
    return 0;
}
