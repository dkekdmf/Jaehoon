#include <stdio.h>
#pragma warning(disable:4996)

int main_whileprac(void) {

	int i = -15;
	while (i <= 20){
		if(i<0){
			if (-i % 2 == 1) {
				printf("%d\n", i);
			}
		}
		if (i >= 0) {
			if (i % 2 == 0) {
				printf("%d\n", i);
			}
		}

		i++;
	}

	return 0;
}