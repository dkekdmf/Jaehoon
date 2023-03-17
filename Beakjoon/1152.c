#include<stdio.h>
#include<string.h>
#pragma warning(disable:4996)

int main_1152(void) {


	char N[1000000];
	int count = 0;
	scanf("%[^\n]", N);
	int len = strlen(N);
	
	if (len == 1) {
		if (N[0] == ' ') {
			printf("0\n");
			return 0;
		}
	}
	for (int i = 1; i < len-1; i++) {

		if (N[i] == ' ') 
			count++;
			
		
		
	}
	printf("%d\n", count+1);
	return 0;
}