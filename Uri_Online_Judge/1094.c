#include <stdio.h>
 
int main() {
 
 int n,i,c=0,s=0,r=0,num;
	char cobaia;
	float tc,tr,ts;

	scanf("%d", &n);

	for(i=1;i<=n;i++){
		scanf("%d %c", &num, &cobaia);

		if(cobaia=='C'){
			c=c+num;
		}
		else if(cobaia=='R'){
			r=r+num;
		}
		else if(cobaia=='S'){
			s=s+num;
		}
	}

	tc = (c*100.00)/(c+r+s);
	tr = (r*100.00)/(c+r+s);
	ts = (s*100.00)/(c+r+s);

	printf("Total: %d cobaias\n", (c+r+s));
	printf("Total de coelhos: %d\n", c);
	printf("Total de ratos: %d\n", r);
	printf("Total de sapos: %d\n",s);
	printf("Percentual de coelhos: %.2f %%\n", tc);
	printf("Percentual de ratos: %.2f %%\n", tr);
	printf("Percentual de sapos: %.2f %%\n", ts);
 
    return 0;
}
