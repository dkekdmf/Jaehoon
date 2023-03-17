#include <stdio.h>
#pragma warning(disable:4996)

int main_1090(void) {

	long long int a, b, c;
	scanf("%lld %lld %lld", &a, &b, &c);

	for (int i = 1; i < c; i++) {
		a *= b;
	}
	printf("%lld", a);
	return 0;
}