#include <stdio.h>
#pragma warning(disable:4996)

int main(void) {
	int a;
	
	
	scanf("%d", &a);

	for (int i = 1; i <= a; i++) {
		int sum = 0;
		for (int j = 0; j < 10; j++) {
			int b;
			scanf("%d", &b);
			
			if (b % 2 == 1)
				sum += b;

		}
		printf("#%d %d ",i, sum);
		}
		
		
//	}


	return 0;
}