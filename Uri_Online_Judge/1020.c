#include <stdio.h>
 
int main() {
 
int n,ano,mes,dia,aux;

	scanf("%d", &n);


		ano = n/365;
		aux = n%365;
		mes = aux/30;
		dia = aux%30;

	printf("%d ano(s)\n", ano);
	printf("%d mes(es)\n", mes);
	printf("%d dia(s)\n", dia);
 
    return 0;
}
