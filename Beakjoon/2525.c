#include <stdio.h>
#pragma warning(disable:4996)

int main_2525(void) {

	int a, b,c;
	int x, y,w, z;
	scanf("%d %d", &a, &b);
	scanf("%d", &c);

	if (b + c < 60) {
		printf("%d %d",a, c +b);
	}
	else if (a<23&&b + c > 60) {
		x = a + (b + c) / 60;
		y = (c - 60 + b - 60);
		printf("%d %d", x, y);
	}
	else if (a >= 23 && b + c > 60) {
		z = a - 23;
		w = (c +b- 60);
		printf("%d %d", z,w);	}
}