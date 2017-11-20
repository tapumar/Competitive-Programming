#include <stdio.h>
 
int main() {
 
 int n,i,j;
	int matriz[70][70];


	while(scanf("%d",&n)!=EOF){
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){

				if(i==j)
					matriz[i][j]=1;
				if((i+j)==(n-1))
					matriz[i][j]=2;
				if(i!=j && (i+j)!=(n-1))
					matriz[i][j]=3;
			}
		}

		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				printf("%d",matriz[i][j]);
			}
			printf("\n");
		}

	}
 
    return 0;
}
