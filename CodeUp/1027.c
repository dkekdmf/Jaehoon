#include <stdio.h>
#pragma warning(disable:4996)

int main_1027(void) {
	int a, b, c;
	scanf("%d.%d.%d", &a, &b, &c);
	printf("%02d-%02d-%04d", c, b, a);

	return 0;
}