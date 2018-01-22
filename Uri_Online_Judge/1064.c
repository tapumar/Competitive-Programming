#include <stdio.h>
 
int main() {
 
 int i,quant;
	float num,media;
	quant=0;
	media=0;

	for(i=0;i<6;i++){
		scanf("%f", &num);
		if(num>0){
			media = media+num;
			quant++;
		}
	}
	media = media/quant;
	printf("%d valores positivos\n", quant);
	printf("%.1f\n",media);
 
    return 0;
}
