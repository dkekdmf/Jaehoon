#include <stdio.h>
#pragma warning(disable:4996)

int main_2908(void) {


	int a,b;
	int c,d,f,g,h,i,j,k;
	int max = 0;

	scanf("%d %d", &a,&b);//432
	
		c = a % 10*100;//c ==2
		d = (a / 10)%10*10;//3
		f = (a / 100);
		g = c + d + f;
		
		h = b % 10 * 100;//c ==2
		i = (b / 10) % 10 * 10;//3
		j = (b / 100);
		k = h+i+j;

		
		if (g > k) {
			max = g;
		}
		else
			max = k;
		printf("%d", max);

	return 0;
}