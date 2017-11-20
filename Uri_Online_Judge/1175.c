#include <stdio.h>
 
int main() {
 
 int vetor[20],i,aux,j;

	for(i=0;i<20;i++){

		scanf("%d",&vetor[i]);
	}
	j=19;
	for(i=0;i<10;i++){
		aux=vetor[i];
		vetor[i]=vetor[j];
		vetor[j]=aux;
		j--;
	}
	for(i=0;i<20;i++){
		printf("N[%d] = %d\n", i,vetor[i]);
	}
 
    return 0;
}
