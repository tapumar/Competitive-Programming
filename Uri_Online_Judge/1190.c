#include <stdio.h>

int main() {

	char ope;
	int col,lin,i=11;
	double matriz[12][12];
	double soma=0,media;

	scanf("%c", &ope);
	
	for(lin=0;lin<12;lin++){
		for(col=0;col<12;col++){
			scanf("%lf", &matriz[lin][col]);
		}
	}


	for(lin=0;lin<12;lin++){
		for(col=i+1;col<12;col++){
			if(col>6 && lin<col){
				soma += matriz[lin][col];
			}
		}
		i--;
	}

	if(ope == 'M'){
		media = soma/30;
		printf("%.1lf\n", media);
	}
	else {
		printf("%.1lf\n", soma);
	}


return 0;
}
