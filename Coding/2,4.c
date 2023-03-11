#include <stdio.h>
#pragma warning(disable:4996)

int main(void) {
	int i;
	printf("start!\n");
	for (i = 0; i <= 20; i++) {

		if (i % 2 == 0) 
			continue;
		
		printf("%d\n", i);
	}
	printf("end!\n");
}