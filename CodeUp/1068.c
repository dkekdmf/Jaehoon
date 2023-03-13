#include <stdio.h>
#pragma warning(disable:4996)

int main_1068(void) {

	int a;
	scanf("%d", &a);

	if (a >= 90 && a <= 100) {
		printf("A");

	}
	if (a >= 70 && a <= 89) {
		printf("B");

	}
	if (a >= 40 && a <= 69) {
		printf("C");

	}
	if(a>=0&&a<=39){
		printf("D");

	}
	return 0;
}