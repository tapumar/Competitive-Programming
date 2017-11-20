#include <stdio.h>

double calcularRaiz(int rep){
    if(rep == 0){
        return 0;
    }
    else{
        rep--;
        return 1/(2+calcularRaiz(rep));
    }
}
 
int main() {
    
    int rep;
    double raiz;
 
   scanf("%d", &rep);

    raiz=calcularRaiz(rep);
    
    raiz = 1.0 + raiz;
    printf("%.10lf\n", raiz);
    
    return 0;
    
}
