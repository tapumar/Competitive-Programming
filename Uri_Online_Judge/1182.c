#include <stdio.h>
 
int main() {
 
 
	float matriz[12][12];
	float soma=0, media=0;
	int i,j,coluna;
	char ope;

	scanf("%d",&coluna);
	getchar();
	scanf("%c",&ope);
	getchar();

	for(i=0;i<12;i++){
		for(j=0;j<12;j++){
			scanf("%f", &matriz[i][j]);
		}
	}
		
	for(i=0;i<12;i++){
		soma=soma+matriz[i][coluna];
	}

	if(ope=='S'){
		printf("%.1f\n", soma);
	}
	else{
		media=soma/12;
		printf("%.1f\n", media);
	}
 
    return 0;
}
