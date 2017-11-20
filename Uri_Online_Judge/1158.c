#include <stdio.h>
 
int main() {
 
  int n,x,y,i,soma,aux;

	scanf("%d",&n);

	for(i=1;i<=n;i++){
		scanf("%d %d",&x,&y);
		aux=0;
		soma=0;
		while(aux<y){
			if(x%2!=0){
				soma=soma+x;
				aux++;
			}
			x++;

		}
	printf("%d\n",soma);
	
	}
 
    return 0;
}
