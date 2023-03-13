#include <stdio.h>
#pragma warning(disable:4996)

int main_1056(void) {
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", (a && !b) || (!a && b));

	return 0;
}