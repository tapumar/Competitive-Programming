#include <stdio.h>
 
int main() {
 
int x,y,i,soma=0;

	scanf("%d",&x);
	scanf("%d",&y);

	if(x>y){
		for(i=y;i<=x;i++){
			if(i%13!=0){
				soma=soma+i;
			}
		}
	}
	else{
		for(i=x;i<=y;i++){
			if(i%13!=0){
				soma=soma+i;
			}
		}
	}
	printf("%d\n",soma);
 
    return 0;
}
