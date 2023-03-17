#include <stdio.h>
#pragma warning(disable:4996)

int main_re25304(void) {
	int price, cost;
	int a, b;
	int plus = 0;
	scanf("%d", &price);
	scanf("%d", &cost);

	for (int i = 0; i < cost; i++) {
		scanf("%d %d", &a, &b);
		plus += a * b;
	}
	if (plus == price) {
		printf("Yes");
	}
	else {
		printf("No");
	}
}