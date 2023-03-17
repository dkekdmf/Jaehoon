#include <stdio.h>
#pragma warning(disable:4996)

int main_10807(void) {

	int N;
	int a[100];
	int v;
	int count = 0;
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		scanf("%d ", &a[i]);
	}
		
		scanf("%d", &v);
		for (int i = 0; i < N; i++) {
	
		if (a[i]==v) {
	  	count++;
		}
		
	}
		printf("%d", count);
	


	return 0;
}