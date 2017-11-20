#include <stdio.h>
 
int main() {
 
	int i,prod,qnt,n;
	float valor=0;

	scanf("%d",&n);

	for(i=0;i<n;i++){
		scanf("%d %d",&prod,&qnt);

		if(prod==1001)
			valor=valor+(qnt*1.5);
		if(prod==1002)
			valor=valor+(qnt*2.5);
		if(prod==1003)
			valor=valor+(qnt*3.5);
		if(prod==1004)
			valor=valor+(qnt*4.5);
		if(prod==1005)
			valor=valor+(qnt*5.5);
	}
	printf("%.2f\n",valor);
 
    return 0;
}
