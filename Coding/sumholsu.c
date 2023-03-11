#include <stdio.h>
#pragma warning(disable:4996)

int main_sumholsu(void) {
	int a;
	int sum = 0;
	printf("정수입력: ");
	scanf("%d", &a);

	for (int i = 1; i <= a; i+=2) {
		
		sum += i;
		
		
		//if (i % 2 == 0)
		//	continue;
		//

		//if (i % 2 == 1) {
		//	sum += i;
		//}
		
	}
	printf("sum1: %d", sum);


	return 0;
}