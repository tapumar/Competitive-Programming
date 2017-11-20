#include <stdio.h>
 
int main() {
 
 char input[80];
	 char input2[80];
	 char input3[80];
	 scanf(" %s", input);
	 scanf(" %s", input2);
	 scanf(" %s", input3);
	 if(!strcmp(input, "vertebrado")){
	 	if(!strcmp(input2, "ave")){
	 		if(!strcmp(input3, "carnivoro")){
	 			printf("aguia\n");
	 		}
	 		if(!strcmp(input3, "onivoro")){
	 			printf("pomba\n");
	 		}
	 	}
	 	if(!strcmp(input2, "mamifero")){
	 		if(!strcmp(input3, "onivoro")){
	 			printf("homem\n");
	 		}
	 		if(!strcmp(input3, "herbivoro")){
	 			printf("vaca\n");
	 		}
	 	}
	 }
	 if(!strcmp(input, "invertebrado")){
	 	if(!strcmp(input2, "inseto")){
	 		if(!strcmp(input3, "hematofago")){
	 			printf("pulga\n");
	 		}
	 		if(!strcmp(input3, "herbivoro")){
	 			printf("lagarta\n");
	 		}
	 	}
	 	if(!strcmp(input2, "anelideo")){
	 		if(!strcmp(input3, "hematofago")){
	 			printf("sanguessuga\n");
	 		}
	 		if(!strcmp(input3, "onivoro")){
	 			printf("minhoca\n");
	 		}
	 	}
	 }
    return 0;
}
