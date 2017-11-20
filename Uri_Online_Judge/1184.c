#include <stdio.h>

int main() {

	char ope;
	int col,lin;
	float matriz[12][12];
	float soma=0,media;

	scanf("%c", &ope);

	for(lin=0;lin<12;lin++){
		for(col=0;col<12;col++){
			scanf("%f", &matriz[lin][col]);
		}
	}


	for(lin=0;lin<12;lin++){
		for(col=0;col<lin;col++){
			soma += matriz[lin][col];
		}
	}
	if(ope == 'M'){
		media = soma/66;
		printf("%.1f\n", media);
	}
	else {
		printf("%.1f\n", soma);
	}


return 0;
}
