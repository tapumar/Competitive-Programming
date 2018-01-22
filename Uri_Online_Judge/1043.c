#include <stdio.h>
 
int main() {
 
float a,b,c,area,peri;

	scanf("%f %f %f", &a,&b,&c);

	if(a<b+c && b<a+c && c<a+b){
		peri = a+b+c;
		printf("Perimetro = %.1f\n", peri);
	}
	else {
		area = ((a+b)*c)/2;
		printf("Area = %.1f\n", area);
	}
 
    return 0;
}
