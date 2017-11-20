#include <stdio.h>
 
int main() {
 
int vetor[10], i, n;
	 scanf("%d", &n);
	 for (i=0; i<10; i++){
	 	if (i==0)
	 		vetor[i] = n;
	 	else 
	 		vetor[i] = vetor[i-1]*2;
	 }
	 for (i=0; i<10; i++)
	 	printf("N[%d] = %d\n", i, vetor[i]);
    return 0;
}
