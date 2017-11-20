#include <stdio.h>
 
int main() {
 
   int n,i,maior,aux;
	maior=0;

	for(i=1;i<=100;i++){
		scanf("%d",&n);
		if(n>maior){
			maior=n;
			aux=i;
		}
	}
	printf("%d\n",maior);
	printf("%d\n", aux);
 
    return 0;
}
