#include <stdio.h>
#pragma warning(disable:4996)

int main_1080(void) {

	int i,a = 0;
	int sum = 0;
	scanf("%d", &a);

	for (i = 1;; i++) {
		sum += i;
		if (sum >= a) {
			break;
		}
		
	}
	printf("%d", i);
	return 0;
	
}