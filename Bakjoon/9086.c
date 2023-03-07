#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

int main_9086(void) {

	int N;
	char munja[100];
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		scanf("%s", munja);
		printf("%c%c\n", munja[0], munja[strlen(munja) - 1]);
		
	}

	return 0;
}