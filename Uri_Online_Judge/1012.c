#include <stdio.h>
 
int main() {
 
 float A,B,C,triangulo,circulo,trapezio,quadrado,retangulo;

	scanf("%f %f %f", &A,&B,&C);

	triangulo = (A*C)/2;

	circulo = 3.14159*(C*C);

	trapezio = ((A+B)*C)/2;

	quadrado = (B*B);

	retangulo = (A*B);

	printf("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f\n", triangulo, circulo, trapezio, quadrado, retangulo);
    return 0;
}
