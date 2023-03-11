#include <stdio.h>
#pragma warning(disable:4996)

int main_starcoding2(void) {

	for (int i = 0; i <= 5; i++) {

		for (int j = 5; j > i; j--) {
			printf("*");
		}
		printf("\n");
	}

	return 0;
}