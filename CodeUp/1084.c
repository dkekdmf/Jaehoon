#include <stdio.h>
#pragma warning(disable:4996)

int main_1084(void) {

	int i, j, k;
	int r, g, b;
	int count = 0;
	scanf("%d %d %d", &r, &g, &b);

	for (i = 0; i < r; i++) {
		for (j = 0; j < g; j++) {
			for (k = 0; k < b; k++) {
				printf("%d %d %d\n", i, j, k);
				count++;
			}
		}
	}
	printf("%d", count);
	return 0;
}