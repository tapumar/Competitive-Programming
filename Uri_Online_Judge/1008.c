#include <stdio.h>
 
int main() {
 
int func, horas;
	float valor,salario;

	scanf("%d", &func);
	scanf("%d", &horas);
	scanf("%f", &valor);

	salario = (horas*valor);

	printf("NUMBER = %d\nSALARY = U$ %.2f\n", func,salario);
    return 0;
}
