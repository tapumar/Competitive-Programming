#include <stdio.h>
 
int main() {
    int a,n,m;
 
scanf("%d %d", &n, &m);

while (n!=0 && m!=0){
    a = m-n;
    if(a==4 || a ==7 || a==10 || a==12 || a==15 || a==20 || a==22 || a==25 || a==30 || a==40 || a==52 || a==55 || a==60 || a==70 || a==100 || a==102 || a==105 || a==110 || a==120 || a==150 || a==200){
        printf("possible\n");
    }
    else{
        printf("impossible\n");
    }
    scanf("%d %d", &n,&m);
}
    return 0;
}
