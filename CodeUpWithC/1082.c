#include <stdio.h>
#pragma warning(disable:4996)

int main_1082(void) {

	int c;
	scanf("%X", &c);

	for (int i = 1; i <= 15; i++) {
		printf("%X*%X=%X\n", c, i, c * i);
	}
	
	return 0;
}