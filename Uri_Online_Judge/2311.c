#include <stdio.h>

int main(){

	int comp,i,j,k,g,x,y;
	float grau,maior,menor,soma;
	float vetor[8];
	char nome[20];

	scanf("%d", &comp);

	for(i=0;i<comp;i++){
		soma=0;
		menor=100;
		maior=0;
		scanf("%s", nome);
		scanf("%f", &grau);
		for(j=0;j<7;j++){
			scanf("%f", &vetor[j]);
		}
		for (k = 0; k < 7; k++) {
        	if (vetor[k] > maior){
				maior = vetor[k];
				x=k;
        	}
        	if (vetor[k] < menor) {
        		menor = vetor[k];
        		y=k;
    		}
    	}
   		for(g = 0;g < 7; g++){
   			if(g != x && g != y){
   				soma = soma + vetor[g];
   			}
   		} 
		soma = soma*grau;
		printf("%s %.2f\n", nome, soma);
	}

return 0;
}
