#include <stdio.h>
 
int main() {
 
 int horai,mini,horaf,minf,durah,duram;

	scanf("%d %d %d %d", &horai,&mini,&horaf,&minf);

	if(horaf>horai){
		durah = horaf - horai;
	}
	else{
		durah = (24 - horai) + horaf;
	}
	if(minf>=mini){
		duram = minf - mini;
	}
	else{
		if(horaf>=horai){
			durah--;
		}
		else{
			durah--;
		}
		duram = (60- mini) + minf;
	}

	printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", durah,duram);
   
    return 0;
}
