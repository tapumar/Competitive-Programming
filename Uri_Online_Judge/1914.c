#include <stdio.h>
#include <string.h>

int main() {

 	long long int num1, num2;
 	int casos, i;

	char nome1[101], nome2[101];
	char jog1[6], jog2[6];

	scanf("%d", &casos);

	for(i=0; i<casos; i++){

		scanf("%s %s %s %s", nome1, jog1, nome2, jog2);
		scanf("%lld %lld", &num1, &num2);

		if(((num1+num2)%2) != 0){
			if(strcmp(jog1,"IMPAR")==0){
				printf("%s\n", nome1);
			}
			else{
				printf("%s\n", nome2);
			}
		}
		else{
			if(strcmp(jog1,"PAR")==0){
				printf("%s\n",nome1);
			}
			else{
				printf("%s\n",nome2);
			}
		}
	}
return 0;
}
