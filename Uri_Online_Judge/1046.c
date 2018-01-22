#include <stdio.h>
 
int main() {
 
   int inicio,final,dura;

	scanf("%d %d", &inicio, &final);

	if(final<=inicio) {

		dura = (24 - inicio) + final;
	} 
	else {
		dura = final - inicio;
	}
	printf("O JOGO DUROU %d HORA(S)\n",dura);

 
    return 0;
}
