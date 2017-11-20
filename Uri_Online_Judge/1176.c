#include <stdio.h>
 
int main() {
 
long long int vetor[61],i,t,n;

	vetor[0]=0;
	vetor[1]=1;

	for(i=2;i<=60;i++){
		vetor[i] = vetor[i-1]+vetor[i-2];
	}

	scanf("%lld",&t);

	for(i=0;i<t;i++){
		scanf("%lld",&n);
		printf("Fib(%lld) = %lld\n",n,vetor[n]);
	}
    return 0;
}
