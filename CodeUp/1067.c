#include <stdio.h>
#pragma warning(disable:4996)

int main_1067(void) {

	int a;
	scanf("%d", &a);

	if (a < 0) {
		printf("minus\n");
		if (a % 2 == 0) {
			printf("even\n");
		}
		else
			printf("odd\n");
	}

	if (a > 0) {
		printf("plus\n");
		if (a % 2 == 0) {
			printf("even\n");
		}
		else
			printf("odd\n");
	}

	
	
}