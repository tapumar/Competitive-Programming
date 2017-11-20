#include <stdio.h>

int main() {

	int A,B,C;

	scanf("%d %d %d", &A, &B, &C);

	if(B<A){
		
		if((C>=B)){
			printf(":)\n");
		}
		else if(((B-C) < (A-B))){
			printf(":)\n");
		}
		else{
			printf(":(\n");
		}
	}
	else if(B>A){
		if((C<=B)){
			printf(":(\n");
		}
		else if ((C-B) < (B-A)){
			printf(":(\n");
		}
		else{
			printf(":)\n");
		}
	}
	else{
		if(C>B){
			printf(":)\n");
		}
		else{
			printf(":(\n");
		}
	}
return 0;
}
