#include <stdio.h>
#pragma warning(disable:4996)

int main_1046(void) {
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);

	printf("%d\n", a + b + c);
	printf("%.1f\n", (float)(a + b + c) / 3);


	return 0;
}