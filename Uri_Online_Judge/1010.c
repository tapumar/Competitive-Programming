#include <stdio.h>
 
int main() {
 
 float valorp1,valorp2,total;
	int codp1,nump1,codp2,nump2;

	scanf("%d %d %f", &codp1, &nump1, &valorp1);
	scanf("%d %d %f", &codp2, &nump2, &valorp2);

	total = (nump1*valorp1) + (nump2*valorp2);

	printf("VALOR A PAGAR: R$ %.2f\n", total);
 
    return 0;
}
