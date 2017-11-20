#include <stdio.h>
 
int main() {
 
int idade,soma=0,cont=0;
	float media;

	scanf("%d",&idade);

	while(idade>=0){
		soma=soma+idade;
		cont++;
		scanf("%d",&idade);
	}
	media=(float)soma/cont;

	printf("%.2f\n",media);
 
    return 0;
}
