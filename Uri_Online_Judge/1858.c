#include <stdio.h>
 
int main() {
 
	int t,n,i,menor=0,aux;
	
	scanf("%d",&t);

	scanf("%d",&n);
	menor=n;
	aux=1;
	for(i=1;i<t;i++){
		scanf("%d",&n);
		if(n<menor){
			menor=n;
			aux=i+1;
		}
	}
	printf("%d\n",aux);
 
    return 0;
}
