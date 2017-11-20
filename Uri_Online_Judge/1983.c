#include <stdio.h>
 
int main() {
 
	int mat,i,n,mmat;
	float nota,maior=0;

	scanf("%d",&n);

	for(i=0;i<n;i++){
		scanf("%d %f",&mat,&nota);
		if(nota>maior){
			maior=nota;
			mmat=mat;
		}
	}
	if(maior>=8.0){
		printf("%d\n",mmat);
	}
	else{
		printf("Minimum note not reached\n");
	}
 
    return 0;
}
