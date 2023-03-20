#include <stdio.h>
#pragma warning(disable:4996)

int main_1093(void) {

	int a[24] = { 0, };
	int n,t;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &t);
		a[t] += 1;
	}
	for (int i = 1; i < 24; i++) {
		printf("%d ", a[i]);
	}
}