#include <stdio.h>
 
int main() {
 
double a, b, c, delta, x1, x2;
	scanf(" %lf %lf %lf", &a, &b, &c);
	delta = (b*b) - (4*a*c);
	if (delta >=0 && a != 0){
		delta = sqrt(delta);
		x1 = (-b + delta) / (2*a);
		x2 = (-b - delta) / (2*a);
		printf("R1 = %.5lf\n", x1);
		printf("R2 = %.5lf\n", x2);
	}
	else{ 
		printf("Impossivel calcular\n");
	}
 
    return 0;
}
