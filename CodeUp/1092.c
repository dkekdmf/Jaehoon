#include <stdio.h>
#pragma warning(disable:4996)

int main_1092(void) {
	int a, b, c;
	int day = 1;
	scanf("%d %d %d", &a, &b, &c);
	while (day % a!= 0 || day % b != 0 || day % c != 0) 
		day++; 
	printf("%d", day);

	return 0;
}