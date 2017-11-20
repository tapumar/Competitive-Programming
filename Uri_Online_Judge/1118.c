#include <stdio.h>
 
int main() {
 
 int p=1;
	float n1,n2,media;

	while(p==1){

		scanf("%f",&n1);
	while(n1<0 || n1>10){
		printf("nota invalida\n");
		scanf("%f", &n1);
	}
	scanf("%f",&n2);
	while(n2<0 || n2>10){
		printf("nota invalida\n");
		scanf("%f",&n2);
	}
	media = (n1+n2)/2;

	printf("media = %.2f\n", media);
	printf("novo calculo (1-sim 2-nao)\n");
	scanf("%d",&p);
	while(p!=1 && p!=2){
		printf("novo calculo (1-sim 2-nao)\n");
		scanf("%d",&p);
	}
	}
 
    return 0;
}
