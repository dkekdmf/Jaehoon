#include <stdio.h>
#pragma warning(disable:4996)

int main(void) {
	int arr[20][20] = { 0, };
	int n,a,x,y;



	for (int i = 1; i <= 19; i++) 
		for (int j = 1; j <= 19; j++) 
			scanf("%d", &arr[i][j]);
			
		
		
	
	scanf("%d", &a);
	for (int i = 1; i <= a; i++) {
		scanf("%d %d", &x, &y);
		for (int j = 1; j <= 19; j++) {
			if (arr[x][j] == 0)
				arr[x][j] = 1;
			else
				arr[x][j] = 0;

		}
		for (int k = 1; k <= 19; k++) {
			if (arr[k][y] == 0)
				arr[k][y] = 1;
			else
				arr[k][y] = 0;

		}
	
	}
    for (int i = 1; i <=19; i++) {
		for (int j = 1; j <= 19; j++) {

			printf("%d ", arr[i][j]);
		}
		printf("\n");
	}
	return 0;
}