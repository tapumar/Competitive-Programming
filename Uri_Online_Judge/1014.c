#include <stdio.h>
 
int main() {
    
    int X;
	float Y,consumo;

	scanf("%d", &X);
	scanf("%f", &Y);

	consumo = (X/Y);

	printf("%.3f km/l\n", consumo);

    return 0;
}
