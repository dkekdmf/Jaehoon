#include <stdio.h>
#pragma warning(disable:4996)

int main_1094(void) {

	int a[1000] = { 0, };
	int	b,c;
	scanf("%d", &c);
	for (int i = 1; i <= c; i++) {
		scanf("%d", &a[i]);
	
	}
	for (int i = c; i >= 0; i--) {
		printf("%d ", a[i]);
	}

}