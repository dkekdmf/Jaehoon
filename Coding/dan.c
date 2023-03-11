#include<stdio.h>
#pragma warning(disable:4996)

int main_danfor(void) {

	int dan;
	printf("dan:");
	scanf("%d", &dan);

	for (int i = 1; i <= 9; i++) {

		printf("%d*%d = %d\n", dan, i, dan * i);
	}



	return 0;
}