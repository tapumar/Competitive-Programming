#include <stdio.h>
#include <string.h>
 
int main() {

	char nome[15];
	int c,n,i;

	scanf("%d",&c);

	for(i=0;i<c;i++){
		scanf("%s %d", nome, &n);
		if(strcmp("Thor",nome)==0){
			printf("Y\n");
		}
		else
			printf("N\n");

	}
 
    return 0;
}
