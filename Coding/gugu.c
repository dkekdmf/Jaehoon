#include <stdio.h>
#pragma warning(disable:4996)

int main_gugufor(void) {

	int a, b;
   
	for (int i = 1; i <= 9; i++) {
		for (int j = 2; j <= 9; j++)
		{
			printf("%d*%d=%2d\n", j, i, i * j);
		}
		
		printf("\n");
	}


	return 0;
}