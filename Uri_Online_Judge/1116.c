#include <stdio.h>
 
int main() {
 
    float div;
	int x,y,n,i;

	scanf("%d",&n);

	for(i=1; i<=n;i++){
		scanf("%d %d", &x,&y);

		if(y==0){
			printf("divisao impossivel\n");
		}
		else{
			div = (float) x/y;
			printf("%.1f\n", div);
		}
	}
 
    return 0;
}
