#include <stdio.h>
 
int main() {
 
	int i,p,n,c,d,e=0;

	scanf("%d %d",&p,&n);

	scanf("%d",&d);

	for(i=1;i<n;i++){
		scanf("%d",&c);
		if(c>(d+p) || c<(d-p)){
			e++;
		}
		d=c;
	}
	if(e==0){
		printf("YOU WIN\n");
	}
	else{
		printf("GAME OVER\n");
	}
    return 0;
}
