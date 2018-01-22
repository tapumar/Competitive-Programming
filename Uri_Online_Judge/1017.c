#include <stdio.h>
 
int main() {
 
int a,b;
	float litros;

	scanf("%d", &a);
	scanf("%d", &b);

	litros = (float)(a*b)/12;

	printf("%.3f\n", litros);
 
    return 0;
}
