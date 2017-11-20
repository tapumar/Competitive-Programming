#include <stdio.h>
 
int main() {
 
int N100 = 0, N50 = 0, N20 = 0, N10 = 0, N5 = 0, N2 = 0, M100 = 0, M50 = 0, M25 = 0, M10 = 0, M5 = 0, M1 = 0, AUX = 0;
	 double VALOR = 0, AUX2 = 0;
	 scanf(" %lf", &VALOR);
	 AUX = VALOR;
	 AUX2 = VALOR - AUX;
	 if (AUX >= 100){
	 	N100 = AUX/100;
	 	AUX = AUX%100;
	 }
	 if (AUX >= 50){
	 	N50 = AUX/50;
	 	AUX = AUX%50;
	 }
	 if (AUX >= 20){
	 	N20 = AUX/20;
	 	AUX = AUX%20;
	 }
	 if (AUX >= 10){
	 	N10 = AUX/10;
	 	AUX = AUX%10;
	 }
	 if (AUX >= 5){
	  N5 = AUX/5;
	  AUX = AUX%5;
	}
	if (AUX >= 2){
		N2 = AUX/2;
		AUX = AUX%2;
	}
	M100 = AUX;
	AUX2 *= 100;
	AUX = AUX2;
	if (AUX >= 50){
		M50 = AUX/50;
		AUX = AUX%50;
	}
	if (AUX >= 25){
		M25 = AUX/25;
		AUX = AUX%25;
	}
	if (AUX >= 10){
		M10 = AUX/10;
		AUX = AUX%10;
	}
	if (AUX >= 5){
		M5 = AUX/5;
		AUX = AUX%5;
	}

	 M1 = AUX;
	 printf("NOTAS:\n");
	 printf("%d nota(s) de R$ 100.00\n", N100);
	 printf("%d nota(s) de R$ 50.00\n", N50);
	 printf("%d nota(s) de R$ 20.00\n", N20);
	 printf("%d nota(s) de R$ 10.00\n", N10);
	  printf("%d nota(s) de R$ 5.00\n", N5);
	   printf("%d nota(s) de R$ 2.00\n", N2);
	   printf("MOEDAS:\n");
	   printf("%d moeda(s) de R$ 1.00\n", M100);
	   printf("%d moeda(s) de R$ 0.50\n", M50);
	   printf("%d moeda(s) de R$ 0.25\n", M25);
	   printf("%d moeda(s) de R$ 0.10\n", M10);
	   printf("%d moeda(s) de R$ 0.05\n", M5);
	   printf("%d moeda(s) de R$ 0.01\n", M1);
    return 0;
}
