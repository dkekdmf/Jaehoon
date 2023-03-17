#include <stdio.h>
#pragma warning(disable:4996)

int main_1085(void) {

	long long int h, b, c, s;
	double a;
	scanf("%lld %lld %lld %lld", &h, &b, &c, &s);
	a = h * b * c * s;
	printf("%.1lf MB",a/(8*1024*1024));
	return 0;
}