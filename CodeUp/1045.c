#include <stdio.h>
#pragma warning(disable:4996)

int main_1045(void) {
	int a, b;
	scanf("%d %d", &a, &b);

	printf("%d\n", a + b);
	printf("%d\n", a - b);
	printf("%d\n", a * b);
	printf("%d\n", a / b);
	printf("%d\n", a % b);
	printf("%.2f\n",(float) a / b);
	return 0;

}