#include <stdio.h>
#pragma warning(disable:4996)

int main_1078(void) {
	int a;
	int sum = 0;
	scanf("%d", &a);

	for (int i = 0; i <= a; i++) {
		if (i % 2 == 0)
			sum += i;
		
	}
	printf("%d", sum);

	return 0;
}