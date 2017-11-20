#include <stdio.h>
 
int main() {
 
    int n,j,x,i,soma;


	scanf("%d", &n);

	for(j=0;j<n;j++){
		soma=0;

		scanf("%d",&x);

		for(i=1;i<x;i++){
			if(x%i==0){
				soma=soma+i;
			}
		}
		if(soma==x){
			printf("%d eh perfeito\n",x);
		}
		else {
			printf("%d nao eh perfeito\n",x);
		}
	}
 
    return 0;
}
