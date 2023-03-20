#include <stdio.h>
#pragma warning(disable:4996)

int main_1087(void) {

	int a=0;
	int sum = 0;
	scanf("%d", &a);

	for (int i = 1; ; i++) {
		sum += i;
		if (sum >= a) {
			break;
		
		}
		
	}
	printf("%d", sum);
	return 0;
}