#include <stdio.h>
 
int main() {
 
  int n,i,j,j1,aux=0;
  
  scanf("%d", &n);
  
  scanf("%d",&j);
  for(i=1;i<n;i++){
      scanf("%d", &j1);
      if(j1<j){
        aux = i+1;
          break;
      }
      j = j1;
  }
  printf("%d\n", aux);
 
    return 0;
}
