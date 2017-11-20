#include <stdio.h>
 
int main() {
 
double antigo,novo,porc,aumento;

scanf("%lf %lf",&antigo,&novo);

aumento = novo-antigo;
porc = (float)(aumento*100)/antigo;

printf("%.2lf%%\n",porc);
 
    return 0;
}
