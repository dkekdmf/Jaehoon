#include <stdio.h>
#pragma warning(disable:4996)

int main_1546(void) {

	int N;
	float avg =0;
	int max = 0;
	scanf("%d", &N);
	int score[100];
	

	for (int i = 0; i < N; i++) {
		scanf("%d", &score[i]);
		if (score[i] > max)
			max = score[i];
	}
	for (int i = 0; i < N; i++) {

		avg += (float)score[i] / max * 100;
	}
	printf("%f\n", avg / N);
	return 0;
}