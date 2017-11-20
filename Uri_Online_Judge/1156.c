#include <stdio.h>
 
int main() {
 
 float i,j=2,s=1;

	for(i=3;i<=39;i=i+2){
		s=s+(i/j);
		j=j*2;
	}
	printf("%.2f\n",s);
 
    return 0;
}
