#include <stdio.h>
#pragma warning(disable:4996)

int main_1089(void) {
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);

	for (int j = 1; j < c; j++) {
		a += b;
	}
	printf("%d", a);
	return 0;
}