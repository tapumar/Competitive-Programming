#include <stdio.h>
 
int main() {
 
  int i,num,quant;
	quant=0;

	for(i=0;i<5;i++){
		scanf("%d", &num);
		if(num%2==0){
			quant++;
		}
	}
	printf("%d valores pares\n", quant);
 
    return 0;
}
