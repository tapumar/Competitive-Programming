#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    long long int a; 
    long long int b; 
    long long int c; 
    long long int d;
    long long int e;
    long long int soma[5];
    long long int somaMaior=0, somaMenor=10000000000;
    int i;
    scanf("%lld %lld %lld %lld %lld",&a,&b,&c,&d,&e);
    
    soma[0] = a+b+c+d;
    soma[1] = a+b+c+e;
    soma[2] = a+b+d+e;
    soma[3] = a+c+d+e;
    soma[4] = b+c+d+e;
    
    for(i=0;i<5;i++){
        if(soma[i] > somaMaior){
            somaMaior = soma[i];
        }
        if(soma[i] < somaMenor){
            somaMenor = soma[i];
        }
    }
    
    printf("%lld %lld\n", somaMenor, somaMaior);
   
    return 0;
}
