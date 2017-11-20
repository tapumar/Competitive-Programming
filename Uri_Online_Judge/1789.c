#include <stdio.h>
 
int main() {
 
	int lesma,vel,maior,i,nivel;

	while(scanf("%d",&lesma)!=EOF){
		maior=0;

		for(i=0;i<lesma;i++){
			scanf("%d",&vel);
			if(vel>maior){
				maior=vel;
				if(vel<10)
					nivel=1;
				else if(vel>=10 && vel <20)
					nivel=2;
				else
					nivel=3;
			}
		}
		printf("%d\n",nivel);
	}
    return 0;
}
