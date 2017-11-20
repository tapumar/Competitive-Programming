#include <stdio.h>
 
int main() {
 
int n,x,y,i,j,soma=0;

	scanf("%d", &n);

	for(j=1;j<=n;j++){
		scanf("%d %d", &x,&y);
		soma=0;
		if(x>y){
			for(i=y+1;i<x;i++){
				if(i%2!=0)
					soma=soma+i;
			}
			printf("%d\n",soma);
		}
		else{
			for(i=x+1;i<y;i++){
				if(i%2!=0)
					soma=soma+i;
			}
			printf("%d\n",soma);
		}
	}
    return 0;
}
