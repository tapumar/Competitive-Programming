#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <algorithm>

using namespace std;

int M;


bool comp (int a, int b){
    if (b%M == a%M){ 
        if(abs(a)%2 ==abs(b)%2){
            if (a%2 != 0){ 
                return a > b;
            }else{ 
                return b > a;
            }
        }
        return abs(a)%2 > abs(b)%2; 
    }
    return a%M < b%M;
}

int main()
{
	int N, cont;

	scanf("%d", &N);
	scanf("%d", &M);

	while(N!=0 && M!=0)
	{
		int vetor[N];
		printf("%d %d\n", N, M);

		for(cont=0;cont<N;cont++){
			scanf("%d", &vetor[cont]);
		}

		sort(vetor,vetor+N,comp);

		for(cont=0;cont<N;cont++){
			printf("%d\n", vetor[cont]);
		}

		scanf("%d", &N);
		scanf("%d", &M);

	}
	printf("0 0\n");

	return 0;
}
