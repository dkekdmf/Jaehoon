#include <stdio.h>
#pragma warning(disable:4996)

int main_1088(void) {

	int a;
	scanf("%d", &a);

	for (int i = 0; i <= a; i++) {
		if (i % 3 == 0)
			continue;
		printf("%d ", i);
	}
	



	return 0;
}