#include <stdio.h>
#pragma warning(disable:4996)

int main_1095(void) {

	int a;
	int b[1000] = { 0, };
	int min = 100001;
	scanf("%d", &a);
	for (int i = 0; i < a; i++) {
		scanf("%d", &b[i]);
		//printf("%d", b[i]);
	}
	for (int i = 0; i < a; i++) {
		if (b[i] < min)
			min = b[i];
	}
	printf("%d", min);



	return 0;
}