#include <stdio.h>
#pragma warning(disable:4996)

int main_midterm2(void) {
	int a;
	int count = 0;

	printf("�� �Է� : ");
	scanf("%d", &a);


	if (a < 2 || a > 12) {
		printf("2~12������ ���� �Է����ּ���");
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
	
	printf("�� %d���� ����Դϴ�~ bye~\n", count);
	


	return 0;
}