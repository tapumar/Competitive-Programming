#include <stdio.h>

int main() {

	long long int PA,PB, PAnovo, PBnovo,casos;
	int Panos, i;
	double G1,G2;

	scanf("%lld", &casos);

	for(i = 0; i < casos; i++){
		Panos = 0;

		scanf("%lld %lld %lf %lf", &PA, &PB, &G1, &G2);
		PAnovo = PA;
		PBnovo = PB;
		while(Panos<=100 && PAnovo<=PBnovo){

			PAnovo = PAnovo+(PAnovo*(G1/100));
			PBnovo = PBnovo+(PBnovo*(G2/100));
			Panos++;
		}

		if(Panos>100){
			printf("Mais de 1 seculo.\n");
		}
		else{
			printf("%d anos.\n", Panos);
		}
	}

	return 0;
}
