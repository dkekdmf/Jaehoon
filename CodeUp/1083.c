#include <stdio.h>
#pragma warning(disable:4996)

int main_1083(void) {

	int a;
	scanf("%d", &a);

	for (int i = 1; i <= a; i++) {
		if (i % 3 == 0) {
			printf("X ");
		}
		else
		printf("%d ", i);
	}
}