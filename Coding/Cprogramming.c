#include <stdio.h>
#pragma warning(disable:4996)

int main_midterm(void) {
	int a, b, c;

	printf("세변 입력: ");
	scanf("%d %d %d", &a, &b, &c);

	while (1) {
		if (a <= 0 || b <= 0 || c <= 0) {
			printf("=>양수만 입력하세요.\n");
			printf("세변 입력: ");
			scanf("%d %d %d", &a, &b, &c);

			continue;
		}
		else if (a + b < c || a + c < b || b + c < a) {
			printf("=>올바르지 않은 삼각형\n");
			printf("세변 입력: ");
			scanf("%d %d %d", &a, &b, &c);

			continue;
		}
		if (a == 0 && b == 0 && c == 0) {
			printf("=>종료합니다 bye~");
			return 0;
		}
		else {
			printf("=>올바른 삼각형\n");
			printf("세변 입력: ");
			scanf("%d %d %d", &a, &b, &c);

			continue;
		}
		
	}

	return 0;
}