#include <stdio.h>
#include <string.h>

int main() {

	char entrada[10000];
	char nova[10000];

	int i,j,k;
	int qnt,tam,met;

	scanf("%d", &qnt);

for(k=0;k<qnt;k++){

	scanf(" %[^\n]s", entrada);


	i=0;
	while (entrada[i] != '\0'){
		if((entrada[i] >=97 && entrada[i]<=122) || (entrada[i])>=65 && entrada[i]<=90){
			entrada[i]+=3;
		}
		i++;
	}

	j=0;
	tam = strlen(entrada);

	for(i = tam -1 ; i >= 0; i--){
		nova[j] = entrada[i];
		j++;
	}
	nova[j]='\0';

	tam = strlen(nova);
	met = tam/2;

	for(i=met;i<tam;i++){
		nova[i]-=1;
	}
	
	printf("%s\n", nova);

}

return 0;
}
