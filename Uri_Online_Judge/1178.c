#include <stdio.h>
 
int main() {
 
double vetor[100],aux;
	int i;

	scanf("%lf",&vetor[0]);

	for(i=0;i<100;i++){
		aux = (double)(vetor[i]/2);
		printf("N[%d] = %.4lf\n",i,vetor[i]);
		if(i<100)
			vetor[i+1]=aux;

	}
    return 0;
}
