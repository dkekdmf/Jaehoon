#include <stdio.h>
#pragma warning(disable:4996)

int main_midterm(void) {
	int a, b, c;

	printf("���� �Է�: ");
	scanf("%d %d %d", &a, &b, &c);

	while (1) {
		if (a <= 0 || b <= 0 || c <= 0) {
			printf("=>����� �Է��ϼ���.\n");
			printf("���� �Է�: ");
			scanf("%d %d %d", &a, &b, &c);

			continue;
		}
		else if (a + b < c || a + c < b || b + c < a) {
			printf("=>�ùٸ��� ���� �ﰢ��\n");
			printf("���� �Է�: ");
			scanf("%d %d %d", &a, &b, &c);

			continue;
		}
		if (a == 0 && b == 0 && c == 0) {
			printf("=>�����մϴ� bye~");
			return 0;
		}
		else {
			printf("=>�ùٸ� �ﰢ��\n");
			printf("���� �Է�: ");
			scanf("%d %d %d", &a, &b, &c);

			continue;
		}
		
	}

	return 0;
}