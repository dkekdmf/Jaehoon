#include <stdio.h>
#pragma warning(disable:4996)

int main_25304(void) {

	int price;
	int cost;
	int x, y;
	int res = 0;
	scanf("%d", &price);
	scanf("%d", &cost);
	for (int i = 0; i < cost; i++) {
		scanf("%d %d", &x, &y);
		res += x * y;
	}
	if (res == price) {
		printf("Yes");
	}
	else {
		printf("No");
	}
}