#include <stdio.h>
 
int main() {
 
  int soma,i,j,n,c;

	scanf("%d",&n);

	for(i=0;i<n;i++){
		soma=0;

		scanf("%d",&c);
		for(j=1;j<=c;j++){
			if(j%2!=0){
				soma++;
			}
			else{
				soma--;
			}

		}
		printf("%d\n",soma);
	}
 
    return 0;
}
