#include <stdio.h>
#pragma warning(disable:4996)

int main_sum(void) {

	int a;
	int sum = 0;
	scanf("%d", &a);
	for (int i = 1; i <= a; i++) {

		sum += i;
	}
	printf("sum: %d", sum);


	return 0;
}