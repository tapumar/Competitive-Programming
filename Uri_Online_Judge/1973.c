#include <stdio.h>

int main(){

long long int i,estrela,cont=0,total=0,aux=0,aux1=0,contTotal=0;


scanf("%lld", &estrela);

long long int n;

for(i=0;i<estrela;i++){
	scanf("%lld",&n);
	total = total + n;
	if(n%2 == 0 && cont==0){
	    if(n==0){
	        aux=1;
	    }
		cont = i+1;
	}

	else if(n==1 && cont==0){
	    aux1++;
	}
}
if(cont!=0){
    if(aux1==0){
        if(aux==1){
            contTotal = (cont-1)*2;
        }
        else{
            contTotal = cont + (cont-1);
        }
    }
    else{
        if(aux==1){
            contTotal = cont + (cont-aux1)-2;
        }
        else{
            contTotal = cont + (cont-aux1)-1;
        }
    }
}
else{
    contTotal = estrela;
    cont = estrela;
}
total = total-contTotal;
printf("%lld %lld\n", cont,total);
return 0;
}
