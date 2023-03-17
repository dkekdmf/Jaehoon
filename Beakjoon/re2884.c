#include<stdio.h>
#pragma warning(disable:4996)

int main(void) {

	int a, b, c;

	scanf("%d %d", &a, &b);

	if (a == 0) {
		if (b >=45) {
			printf("%d %d",a, b - 45);
		}
		else if (b < 45) {
			printf("%d %d", a + 23, b + 15);
		}
	}
	if (a > 0) {
		if (b >= 45) {
			printf("%d %d", a,b - 45);
		}
		else if (b < 45) {
			printf("%d %d", a - 1, b + 15);
		}
	}
}