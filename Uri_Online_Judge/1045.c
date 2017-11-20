#include <stdio.h>
 
 
int main() {
double a, b, c;
scanf(" %lf %lf %lf", &a, &b, &c);
if (a<(b+c) && b<(a+c) && c<(a+b)){
	if ((a*a == b*b + c*c) ||  (b*b == a*a + c*c) ||  (c*c == b*b + a*a))
		printf("TRIANGULO RETANGULO\n");
	if ((a*a > b*b + c*c) ||  (b*b > a*a + c*c) ||  (c*c > b*b + a*a))
		printf("TRIANGULO OBTUSANGULO\n");
	if ((a*a < b*b + c*c) &&  (b*b < a*a + c*c) && (c*c < b*b + a*a))
		printf("TRIANGULO ACUTANGULO\n");
	if (a == b && b == c){
		printf("TRIANGULO EQUILATERO\n");
	}
	else if (a==b || b == c || a == c){
		printf("TRIANGULO ISOSCELES\n");
	}
}
else{
	printf("NAO FORMA TRIANGULO\n");
}
 
    return 0;
}
