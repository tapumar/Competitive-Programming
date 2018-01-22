#include <stdio.h>
 
int main() {
 
float salario, aumento, novo;

	scanf("%f", &salario);

	if(salario<=400){
		aumento = salario*0.15;
		novo = aumento + salario;
		printf("Novo salario: %.2f\n", novo);
		printf("Reajuste ganho: %.2f\n", aumento);
		printf("Em percentual: 15 %%\n");
	}
	else if(salario>400 && salario<=800){
		aumento = salario*0.12;
		novo = aumento + salario;
		printf("Novo salario: %.2f\n", novo);
		printf("Reajuste ganho: %.2f\n", aumento);
		printf("Em percentual: 12 %%\n");
	}
	else if (salario>800 && salario<=1200){
		aumento = salario*0.10;
		novo = aumento + salario;
		printf("Novo salario: %.2f\n", novo);
		printf("Reajuste ganho: %.2f\n", aumento);
		printf("Em percentual: 10 %%\n");
	}
	else if(salario>1200 && salario<=2000){
		aumento = salario*0.07;
		novo = aumento + salario;
		printf("Novo salario: %.2f\n", novo);
		printf("Reajuste ganho: %.2f\n", aumento);
		printf("Em percentual: 7 %%\n");
	}
	else if(salario>2000){
		aumento = salario*0.04;
		novo = aumento + salario;
		printf("Novo salario: %.2f\n", novo);
		printf("Reajuste ganho: %.2f\n", aumento);
		printf("Em percentual: 4 %%\n");
	}
 
    return 0;
}
