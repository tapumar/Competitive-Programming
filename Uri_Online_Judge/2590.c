#include  <stdio.h>

int main(void)
{
    int casos,n,i;
    
    scanf("%d",&casos);
    
    for(i=0;i<casos;i++){
        scanf("%d",&n);
        switch(n%4){
            case 0:
                printf("1\n");
                break;
            case 1:
                printf("7\n");
                break;
            case 2:
                printf("9\n");
                break;
            case 3:
                printf("3\n");
                break;
            }
    }
    return 0;
}
