#include <stdio.h>
#pragma warning(disable:4996)

int main_dandowhile(void) {
	int dan;
	int i = 1;
	printf("dan:");
	scanf("%d", &dan);
	do {

		printf("%d*%d = %d\n", dan, i, dan * i);
		i++;
	} while (i <= 9);




	return 0;

}