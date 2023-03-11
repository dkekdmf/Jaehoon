#include <stdio.h>
#pragma warning(disable:4996)

int main_yangquiz1(void) {
	float a, b;
	printf("실수 두개 입력:");
	scanf("%f %f", &a, &b);
	printf("정수부끼리의합:%d",(int)a +(int) b);

	return 0;
}