#include <stdio.h>
#pragma warning(disable:4996)

int main(void) {

	int a[10][10];
	int max = 0;
	int r, c = 0;

		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				scanf("%d", &a[i][j]);
			}
		}
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			
			if (a[i][j] > max) {
				max = a[i][j];
				r = i;
				c = j ;
			}
			

	}
		
	}
	printf("%d \n", max);
	printf("%d %d", r+1, c+1);
	return 0;
}