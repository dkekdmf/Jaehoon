#include <stdio.h>
#pragma warning(disable:4996)

int main_yang3(void) {
	int kor, math, eng;
	scanf("%d %d %d", &kor, &math, &eng);

   int sum = kor + math + eng;
   int avg = (kor + math + eng)/ 3;

   printf("%d %d\n", sum, avg);


}