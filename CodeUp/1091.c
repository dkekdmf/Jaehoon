#include <stdio.h>
#pragma warning(disable:4996)

int main_1091(void) {

	long long int a, m, d, n;

	scanf("%lld %lld %lld %lld", &a, &m, &d, &n);
	for (int i = 1; i < n; i++) {
		a *= m;
		a += d;
	}
	printf("%lld", a);


	return 0;
}