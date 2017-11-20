#include <stdio.h>
 
int main() {
 
int h,m,e,i,casos;
scanf("%d", &casos);
for(i=0;i<casos;i++){
    scanf("%d %d %d", &h,&m,&e);
    if(h==0){
        if(m<10){
            if(e == 0){
                printf("00:0%d - A porta fechou!\n",m);
            }
            else{
                printf("00:0%d - A porta abriu!\n",m);
            }
        }
        else{
            if(e == 0){
                printf("00:%d - A porta fechou!\n",m);
            }
            else{
                printf("00:%d - A porta abriu!\n",m);
            }
        }
    }
    else if(h<10){
        if(m<10){
            if(e == 0){
                printf("0%d:0%d - A porta fechou!\n",h,m);
            }
            else{
                printf("0%d:0%d - A porta abriu!\n",h,m);
            }
        }
        else{
            if(e == 0){
                printf("0%d:%d - A porta fechou!\n",h,m);
            }
            else{
                printf("0%d:%d - A porta abriu!\n",h,m);
            }
        }    
    }
    else{
        if(m<10){
            if(e == 0){
                printf("%d:0%d - A porta fechou!\n",h,m);
            }
            else{
                printf("%d:0%d - A porta abriu!\n",h,m);
            }
        }
        else{
            if(e == 0){
                printf("%d:%d - A porta fechou!\n",h,m);
            }
            else{
                printf("%d:%d - A porta abriu!\n",h,m);
            }
        } 
    }
}
 
    return 0;
}
