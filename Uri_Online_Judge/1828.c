#include <stdio.h>
#include <string.h>

int main() {

	char shel[8];
	char raj[8];

	int teste,i;

	scanf("%d", &teste);

	for(i=0;i<teste;i++){

		scanf("%s %s", shel, raj);

		if(strcmp(shel,raj)==0){
			printf("Caso #%d: De novo!\n",i+1);
		}
		else if(strcmp(shel,"tesoura")==0){
			if(strcmp(raj,"papel")==0 || strcmp(raj,"lagarto")==0){
				printf("Caso #%d: Bazinga!\n",i+1);
			}
			else if(strcmp(raj,"Spock")==0 || strcmp(raj,"pedra")==0){
				printf("Caso #%d: Raj trapaceou!\n",i+1);
			}
		}
		else if(strcmp(shel,"papel")==0){
			if(strcmp(raj,"pedra")==0 || strcmp(raj,"Spock")==0){
				printf("Caso #%d: Bazinga!\n",i+1);
			}
			else if(strcmp(raj,"tesoura")==0 || strcmp(raj,"lagarto")==0){
				printf("Caso #%d: Raj trapaceou!\n",i+1);
			}
		}
		else if(strcmp(shel,"Spock")==0){
			if(strcmp(raj,"tesoura")==0 || strcmp(raj,"pedra")==0){
				printf("Caso #%d: Bazinga!\n",i+1);
			}
			else if(strcmp(raj,"papel")==0 || strcmp(raj,"lagarto")==0){
				printf("Caso #%d: Raj trapaceou!\n",i+1);
			}
		}
		else if(strcmp(shel,"pedra")==0){
			if(strcmp(raj,"lagarto")==0 || strcmp(raj,"tesoura")==0){
				printf("Caso #%d: Bazinga!\n",i+1);
			}
			else if(strcmp(raj,"papel")==0 || strcmp(raj,"Spock")==0){
				printf("Caso #%d: Raj trapaceou!\n",i+1);
			}
		}
		else if(strcmp(shel,"lagarto")==0){
			if(strcmp(raj,"Spock")==0 || strcmp(raj,"papel")==0){
				printf("Caso #%d: Bazinga!\n",i+1);
			}
			else if(strcmp(raj,"tesoura")==0 || strcmp(raj,"pedra")==0){
				printf("Caso #%d: Raj trapaceou!\n",i+1);
			}
		}

	}
return 0;
}
