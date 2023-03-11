#include <stdio.h>
#pragma warning(disable:4996)

int main_danwhile(void) {
	int dan;
	int i =1;
	printf("dan:");
	scanf("%d", &dan);

	while (i <= 9) {

		printf("%d*%d = %d\n", dan, i, dan * i);
		i++;
	}



	return 0;
}