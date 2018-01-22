#include <stdio.h>
 
int main() {
 
 float salario,aux,imp, imp1,imp2,imp3;

	scanf("%f", &salario);

	imp1=0;
	imp2=0;
	imp3=0;

	if(salario>4500.00){
		aux = salario - 4500;
		imp3 = aux*0.28;
		salario = 4500;
	}
	if(salario>3000.00){
		aux = salario - 3000;
		imp2 = aux*0.18;
		salario = 3000;
	}
	if(salario>2000.00) {
		aux = salario - 2000;
		imp1 = aux*0.08;
	}
	if(salario<=2000.00){
		printf("Isento\n");
	}

	imp = imp1+imp2+imp3;

	if(salario>2000){
		printf("R$ %.2f\n", imp);
	}
 
    return 0;
}
