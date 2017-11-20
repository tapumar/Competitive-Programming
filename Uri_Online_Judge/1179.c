#include <stdio.h>
 
int main() {
 
int par[5], impar[5],i,pa=0,im=0,n,j;

	for(i=0;i<15;i++){

		scanf("%d",&n);
		if(pa==5){
			for(j=0;j<=4;j++){
				printf("par[%d] = %d\n",j,par[j]);
			}
			pa=0;
		}
		if(im==5){
			for(j=0;j<=4;j++){
				printf("impar[%d] = %d\n",j,impar[j]);
			}
			im=0;
		}
		if(n%2==0){
			par[pa]=n;
			pa++;
		}
		else{
			impar[im]=n;
			im++;
		}
	}
	if(im!=0){
		for(j=0;j<im;j++){
			printf("impar[%d] = %d\n",j,impar[j]);
		}
	}
	if(par!=0){
		for(j=0;j<pa;j++){
			printf("par[%d] = %d\n",j,par[j]);
		}
	}
    return 0;
}
