#include <stdio.h>
 
int main() {

int senha;

while(scanf("%d", &senha) != EOF){
    senha--;
    printf("%d\n",senha);
}
 
    return 0;
}
