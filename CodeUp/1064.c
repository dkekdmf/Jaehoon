#include <stdio.h>
#pragma warning(disable:4996)

int main_1064(void) {

	int a, b,c;
	scanf("%d %d %d", &a, &b, &c);

	printf("%d", (a < b ? a : b) < c ? (a < b ? a : b) : c);


	return 0;

}