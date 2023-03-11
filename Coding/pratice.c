#include <stdio.h>
#pragma warning(disable:4996)

int main_casting(void) {
	int a, b, c;

	 a = 2;
	 b = 3.9;
	 c = a * b;
	 printf("%d %d %d",a,b,c);
	return 0;
}