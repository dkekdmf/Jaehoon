#include <stdio.h>
#pragma warning(disable:4996)

int main_dowhileprac(void) {
	double a=0;
	do {
	
		printf("실수입력: ");
		scanf("%lf", &a);

		if (a == 9.9) {
			printf("bye~");
			

		}
		
	} while (a!=9.9);




	return 0;
}