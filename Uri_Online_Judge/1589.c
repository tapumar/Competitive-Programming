#include <stdio.h>

int main() {

	int casos, i, r1, r2, raio;


	scanf("%d",&casos);

	for(i=0;i<casos;i++){

		scanf("%d %d", &r1, &r2);

		raio = r1+r2;

		printf("%d\n", raio);

	}
return 0;
}
