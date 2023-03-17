#include <stdio.h>
#pragma warning(disable:4996)

int main(void) {

	int a;
	scanf("%d", &a);
	
	int x = a / 4;
	for (int i = 0; i < x; i++) {
		
		printf("long");
	}
	printf("int");
}