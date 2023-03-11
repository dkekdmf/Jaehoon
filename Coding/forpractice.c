#include <stdio.h>
#pragma warning(disable:4996)

int main_forpractice(void) {

	for (int i = 0; i <= 100; i++) {

		if (i % 3 == 0 && i % 4 !=0) {
			printf("%d\n", i);
		}
	}

	return 0;
}