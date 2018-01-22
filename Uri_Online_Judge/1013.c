#include <stdio.h>
 
int main() {
 
  int MaiorAB, MaiorBC, Maior, A, B, C;

	scanf(" %d %d %d", &A, &B, &C);

	MaiorAB = (A+B + abs(A-B))/2;
	MaiorBC = (B+C + abs(B-C))/2;
	Maior = (MaiorAB + MaiorBC + abs(MaiorAB-MaiorBC))/2;

	printf("%d eh o maior\n", Maior);
    return 0;
}
