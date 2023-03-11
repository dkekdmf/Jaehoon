#include <stdio.h>
#pragma warning(disable:4996)

int main_cyang2(void) {

	float a, b, height;
	scanf("%f %f %f", &a, &b, &height);
	printf("%.1f", (a + b) / 2 * height);


	return 0;
}