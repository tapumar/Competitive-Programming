#include <stdio.h>
 
int main() {
 
  int i,quant;
	float num;
	quant=0;

	for(i=0;i<6;i++){
		scanf("%f", &num);
		if(num>0){
			quant++;
		}
	}
	printf("%d valores positivos\n", quant);
 
    return 0;
}
