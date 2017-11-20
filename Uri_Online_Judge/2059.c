#include <stdio.h>

int main() {

	int p,j1,j2,r,a,soma;

	scanf("%d %d %d %d %d", &p,&j1,&j2,&r,&a);

	soma = j1+j2;

		if(r==1){
			if(a==1){
				printf("Jogador 2 ganha!\n");
			}
			else{
				printf("Jogador 1 ganha!\n");
			}
		}
		else{
			if(a==1){
				printf("Jogador 1 ganha!\n");
			}
			else{
				switch(p){
					case 1:
						if(soma%2 == 0){
							printf("Jogador 1 ganha!\n");
						}
						else{
							printf("Jogador 2 ganha!\n");
						}
					break;
					case 0:
						if(soma%2 == 0){
							printf("Jogador 2 ganha!\n");
						}
						else{
							printf("Jogador 1 ganha!\n");
						}
				}
			}
		}

return 0;	
}
