#include <stdio.h>
 
int main() {
 
  int i,num;

	scanf("%d", &num);

	if(num%2==0){
		num++;
	}

	for(i=num;i<=(num+10);i+=2){
		printf("%d\n",i);
	}
 
    return 0;
}
