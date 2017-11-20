#include <stdio.h>
int main()
{
    
    long long int n;

    scanf("%lld", &n);

    while((n/10) != 0){
        printf("%lld", (n%10));
        n = n/10;
    }
    printf("%lld\n",n);
    return 0;
}
