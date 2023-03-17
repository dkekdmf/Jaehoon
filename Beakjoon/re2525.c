#include <stdio.h>
#pragma warning(disable:4996)

int main_re2525(void) {

	int a, b, c;
	scanf("%d %d", &a, &b);
	scanf("%d", &c);

		if (b + c < 60) {
			printf("%d %d", a, b + c);

    	}
		else {
			int min = (b + c) % 60;
			int hour = (b + c) / 60;

			if (a + hour < 24) {
				printf("%d %d", a+hour, min);
			 }
			else {
				printf("%d %d", a + hour - 24, min);
			}
		}
}
