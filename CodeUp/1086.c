#include <stdio.h>
#pragma warning(disable:4996)

int main_1086(void) {

	int w, h, b;
	scanf("%d %d %d", &w, &h, &b);
	double result = w * h * b;

	printf("%.2lf MB", result/(8*1024*1024));

	return 0;

}