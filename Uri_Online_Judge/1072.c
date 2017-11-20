#include <stdio.h>
 
int main() {
 
 int n,in,out,i;
	float num;
	in=0;
	out=0;

	scanf("%d", &n);

	for(i=0;i<n;i++){
		scanf("%f",&num);
		if(num>=10 && num<=20){
			in++;
		}
		else{
			out++;
		}
	}

	printf("%d in\n",in);
	printf("%d out\n",out);
    return 0;
}
