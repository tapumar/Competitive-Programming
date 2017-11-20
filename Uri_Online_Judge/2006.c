#include <stdio.h>
 
int main() {
 
  
	int n,i,cont=0,nota;

	scanf("%d",&n);

	for(i=0;i<5;i++){
		scanf("%d",&nota);
		if(nota==n)
			cont++;
	}
	printf("%d\n",cont);
    return 0;
}
