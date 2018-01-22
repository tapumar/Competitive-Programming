#include <stdio.h>
 
int main() {
 
char nome[50];
	double fixo,vendas,salario;

	scanf("%s", nome);
	scanf("%lf", &fixo);
	scanf("%lf", &vendas);

	salario = (fixo + (vendas*0.15));

	printf("TOTAL = R$ %.2lf\n", salario);

 
    return 0;
}
