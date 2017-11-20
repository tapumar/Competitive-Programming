#include <stdio.h>
#include <string.h>
 
int main() {
 
char jogador1[7],jogador2[7];
	int teste,i;

	scanf("%d",&teste);

	for(i=0;i<teste;i++){
		scanf("%s",jogador1);
		scanf("%s",jogador2);

		if(strcmp(jogador1,"pedra")==0){
			if(strcmp(jogador2,"pedra")==0){
				printf("Sem ganhador\n");
			}
			else if(strcmp(jogador2,"papel")==0){
				printf("Jogador 1 venceu\n");
			}
			else if(strcmp(jogador2,"ataque")==0){
				printf("Jogador 2 venceu\n");
			}
		}
		else if(strcmp(jogador1,"ataque")==0){

			if(strcmp(jogador2,"pedra")==0){
				printf("Jogador 1 venceu\n");
			}
			else if(strcmp(jogador2,"papel")==0){
				printf("Jogador 1 venceu\n");
			}
			else if(strcmp(jogador2,"ataque")==0){
				printf("Aniquilacao mutua\n");
			}

		}
		else if(jogador1,"papel"){

			if(strcmp(jogador2,"pedra")==0){
				printf("Jogador 2 venceu\n");
			}
			else if(strcmp(jogador2,"papel")==0){
				printf("Ambos venceram\n");
			}
			else if(strcmp(jogador2,"ataque")==0){
				printf("Jogador 2 venceu\n");
			}
		}

	}
 
 
    return 0;
}
