#include <stdio.h>
 
int main() {
 
  int x,y,soma,i;
	soma=0;

	scanf("%d", &x);
	scanf("%d",&y);

	if(x>y){
		for(i=y+1;i<x;i++){
			if(i%2!=0){
				soma=soma+i;
			}
		}
	}
	else if(x<y){
		for(i=x+1;i<y;i++){
			if(i%2!=0){
				soma=soma+i;
			}
		}
	}

	printf("%d\n",soma);
 
    return 0;
}
