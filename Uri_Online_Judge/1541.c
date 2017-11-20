#include <stdio.h>
#include <math.h>

int main() {

	int casa,terreno,A,B,C;
scanf("%d", &A);
while(A != 0){
	scanf("%d %d", &B, &C);

	casa = A*B;
	terreno = (casa*100)/C;
	terreno = sqrt(terreno);

	printf("%d\n", terreno);
	scanf("%d", &A);
}



return 0;
}
