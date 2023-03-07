#include <stdio.h>
#pragma warning(disable:4996)
#include <string.h>
int main_2743(void) {


	char N[100];
	int count = 0;
	scanf("%s", N);

	for (int i = 0; i <strlen(N); i++) {
		
		if (N[i] !=EOF ) {
			count++;
		}
		
	}
	printf("%d", count);

	return 0;
}