#include <stdio.h>
 
int main() {
 
  int N, NH = 0, NM = 0, NS = 0, AUX;
	scanf(" %d", &N);
	AUX = N;
	if (AUX >= 3600){
		NH = AUX/3600;
		AUX = AUX%3600;
	}
	if (AUX >= 60){
		NM = AUX/60;
		AUX = AUX%60;
	}
	NS = AUX;
	printf("%d:%d:%d\n", NH, NM, NS);
	return 0;
 
    return 0;
}
