#include <stdio.h>
 
int main() {
 
  int i=1,j=7,k;

	while(i<=9){
		k=0;
		while(k<3){
			printf("I=%d J=%d\n", i, j);
			j--;
			k++;
		}
		j=j+5;
		i=i+2;
	}
 
    return 0;
}
