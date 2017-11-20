#include <stdio.h>
 
int main() {
int X, Y, i, j;
scanf("%d %d", &X, &Y);
for (i=1; i <= Y-2; NULL) {
	for (j=0; j<X; j++) {
		if(j != X-1)
			printf("%d ", i);
			else
				printf("%d", i);
			i++;
		}
		printf("\n");
}
 
    return 0;
}
