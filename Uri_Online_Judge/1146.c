#include <stdio.h>
 
int main() {
 
int x,i;

	scanf("%d",&x);

	while(x!=0){
		for(i=1;i<x;i++){
			printf("%d ",i);
		}
		printf("%d\n",x);
		scanf("%d",&x);
	}
 
    return 0;
}
