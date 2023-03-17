#include <stdio.h>
#pragma warning(disable:4996)

int main_re10818(void) {

	int N;
	int a[100];
	int max = -100001;
	int min = 100001;
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &a[i]);
	}
	for (int i = 0; i <N; i++)
	{
		

		if (a[i] > max)
			max = a[i];
		if (a[i] < min)
		min = a[i];

	}
	printf("%d %d", max, min);

}