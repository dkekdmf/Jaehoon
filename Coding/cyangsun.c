#include <stdio.h>
#pragma warning(disable:4996)

int main_yangsun1(void) {

	int a,b;
	printf("두각입력: ");
	scanf("%d %d", &a, &b);
	printf("삼각형의 나머지값 %d",180 - (a + b));

	return 0;
}