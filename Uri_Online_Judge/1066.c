#include <stdio.h>
 
int main() {
 
  int num,i, par=0,impar=0,pos=0,neg=0;

	for(i=0;i<5;i++){
		scanf("%d", &num);
		if(num>0){
			pos++;
		}
		else if(num!=0){
			neg++;
		}
		if(num%2==0){
			par++;
		}
		else{
			impar++;
		}
	}
	
	printf("%d valor(es) par(es)\n",par);
	printf("%d valor(es) impar(es)\n",impar);
	printf("%d valor(es) positivo(s)\n",pos);
	printf("%d valor(es) negativo(s)\n",neg);

 
    return 0;
}
