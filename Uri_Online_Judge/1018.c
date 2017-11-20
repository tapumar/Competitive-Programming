#include <stdio.h>
 
int main() {
 
  int VALOR, N100 = 0, N50 = 0, N20 = 0, N10 = 0, N5 = 0, N2 = 0, N1 = 0, AUX;
	 scanf(" %d", &VALOR);
	 AUX = VALOR;
	 if (AUX >= 100)
	 {
	 	 N100 = AUX/100;
	 	  AUX = AUX%100;
	 	}
	 if (AUX >= 50)
	 		{
	 			N50 = AUX/50;
	 			AUX = AUX%50;
	 		}
	 if (AUX >= 20)
	 	{
	 		N20 = AUX/20;
	 		AUX = AUX%20;
	 	}
	 	if (AUX >= 10)
	 	{
	 		N10 = AUX/10;
	 		AUX = AUX%10;
	 	}
	 		if (AUX >= 5){
	 			N5 = AUX/5;
	 			AUX = AUX%5;
	 		}
	 		if (AUX >= 2)
	 			{
	 				N2 = AUX/2;
	 				 AUX = AUX%2;
	 				}
	 				N1 = AUX;
	 				 printf("%d\n", VALOR);
	 				 printf("%d nota(s) de R$ 100,00\n", N100);
	 				 printf("%d nota(s) de R$ 50,00\n", N50);
	 				 printf("%d nota(s) de R$ 20,00\n", N20);
	 				 printf("%d nota(s) de R$ 10,00\n", N10);
	 				 printf("%d nota(s) de R$ 5,00\n", N5); 
					printf("%d nota(s) de R$ 2,00\n", N2);
					 printf("%d nota(s) de R$ 1,00\n", N1);
 
    return 0;
}
