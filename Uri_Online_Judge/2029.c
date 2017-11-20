#include <stdio.h>
 
int main() {
 
	double vol,diam,alt,area,raio;


	while(scanf("%lf",&vol)!=EOF){

		scanf("%lf",&diam);

		raio = diam/2;

		area = (3.14)*(raio)*(raio);

		alt = vol/area;

		printf("ALTURA = %.2lf\n", alt);
		printf("AREA = %.2lf\n", area);
	}
    return 0;
}
