#include <stdio.h>
 
int main() {
 
int a, b, auxiliar, i, n;
a = 0;
b = 1;
scanf("%d", &n);
if (n == 1)
	printf("%d\n", b);
else if (n == 2)
	printf("%d %d\n", a, b);
else {
	printf("%d %d", a, b);
	for(i = 0; i < n-2; i++) {
		auxiliar = a + b;
		a = b;
		b = auxiliar;
		printf(" %d", auxiliar);
	}
}
printf("\n");
    return 0;
}
