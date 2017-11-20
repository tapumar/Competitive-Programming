#include <stdio.h>
 
int main() {
 
 int x,i,n,j,soma;

	scanf("%d",&n);

	for(i=0;i<n;i++){
		soma=0;
		scanf("%d",&x);
		for(j=1;j<x;j++){
			if(x%j==0){
				soma=soma+j;
			}
		}
		if(soma==1){
			printf("%d eh primo\n",x);
		}
		else{
			printf("%d nao eh primo\n",x);
		}
	}
 
    return 0;
}
