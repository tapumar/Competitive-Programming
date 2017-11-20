#include <stdio.h>
 
int main() {
 
 int vetor[1000],i,n,j=0;

	scanf("%d",&n);

	while(j<1000){
		for(i=0;i<n && j<1000;i++){
			vetor[j]=i;
			printf("N[%d] = %d\n",j,vetor[j]);
			j++;

		}
	}
 
    return 0;
}
