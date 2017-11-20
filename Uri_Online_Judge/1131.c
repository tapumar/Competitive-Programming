#include <stdio.h>
 
int main() {
 
    int x,y,gre=0,gremio=0,inter=0,emp=0,maior,p=1;


	while(p==1){
		scanf("%d %d", &x,&y);

		gre++;

		if(x>y){
			inter++;
		}
		else if(x<y){
			gremio++;
		}
		else{
			emp++;
		}

		printf("Novo grenal (1-sim 2-nao)\n");
		scanf("%d",&p);
	}

	printf("%d grenais\n",gre);
	printf("Inter:%d\n",inter);
	printf("Gremio:%d\n",gremio);
	printf("Empates:%d\n",emp);
	if(inter>gremio){
		printf("Inter venceu mais\n");
	}
	else if(gremio>inter){
		printf("Gremio venceu mais\n");
	}
	else{
		printf("Nao houve vencedor\n");
	}
 
    return 0;
}
