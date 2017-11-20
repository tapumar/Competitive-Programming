#include <stdio.h>
 
int main() {
 
 int x,i,soma,aux;

	scanf("%d",&x);

	while(x!=0){
		aux=0;
		soma=0;
		while(aux<5){
			if(x%2==0){
				soma=soma+x;
				aux++;
			}
			x++;
		}
	printf("%d\n",soma);
	scanf("%d",&x);
	
	}
    return 0;
}
