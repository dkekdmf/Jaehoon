#include <stdio.h>
#pragma warning(disable:4996)

int main_guguwhile(void) {
	int i = 2;
	

	while (i <= 9) {
		int j = 1;
		while (j <= 9) {

			printf("%d*%d= %d\n", i, j, i * j);
			j++;
		}
		
		printf("\n");

		i++;
			
	}

	return 0;
}