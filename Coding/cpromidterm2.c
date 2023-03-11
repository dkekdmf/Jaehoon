#include <stdio.h>
#pragma warning(disable:4996)

int main_midterm2(void) {
	int a;
	int count = 0;

	printf("수 입력 : ");
	scanf("%d", &a);


	if (a < 2 || a > 12) {
		printf("2~12사이의 수롤 입력해주세요");
		return 0;
	}


	for (int i = 1; i <= 6; i++) {
		
		
		if (i == a) {
			break;
		}
		if ((a - i) > 6) {
			continue;
		}
		printf("%d %d\n", i, a - i);
		count++;
	}
	
	printf("총 %d개의 경우입니다~ bye~\n", count);
	


	return 0;
}