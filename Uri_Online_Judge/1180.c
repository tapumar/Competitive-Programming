#include <stdio.h>
 
int main() {
 
	int vetor[1000];
	int i,aux,pos,n;

	scanf("%d",&n);

	for(i=0;i<n;i++){
		scanf("%d",&vetor[i]);
	}

	aux=vetor[0];
	pos=0;


	for(i=0;i<n;i++){
		if(vetor[i]<aux){
			aux=vetor[i];
			pos=i;
		}
	}

	printf("Menor valor: %d\n",aux);
	printf("Posicao: %d\n",pos);
 
    return 0;
}
