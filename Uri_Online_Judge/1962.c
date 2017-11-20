#include <stdio.h>
 
int main() {
 
	int n,qnt,ano,i;

	scanf("%d",&n);

	for(i=0;i<n;i++){
		scanf("%d",&qnt);

		if(qnt>=2015){
			ano=qnt-2015;
			printf("%d A.C.\n",ano+1);
		}
		if(qnt<2015){
			ano=2015-qnt;
			printf("%d D.C.\n",ano);
		}
	}
 
    return 0;
}
