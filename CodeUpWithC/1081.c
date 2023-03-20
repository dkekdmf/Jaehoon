#include <stdio.h>
#pragma warning(disable:4996)

int main_1081(void) {

	
	int i, j;
	int n,m;
	scanf("%d %d", &m, &n);
	for (i = 1; i <= m; i++) {
		for (j = 1; j <= n; j++) {
			printf("%d %d\n", i, j);
		}
	}



	return 0;
}