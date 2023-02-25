#include <stdio.h>
#pragma warning(disable:4996)

int main_2884(void) {

	int a, b;
	scanf("%d %d", &a,&b);

	if (a!=0&&b >= 45) {
		printf("%d %d", a, b - 45);
	}
	else if(a != 0 && b< 45){
		int x = a - 1;
		int y =  (b + 60) - 45;
		printf("%d %d", x, y);
		
		
	}
	else if(a==0&& b >= 45){
		printf("%d %d", a + 23, b - 45);

	}
	else if (a == 0 && b < 45) {
		int y = (b + 60) - 45;
		printf("%d %d", a + 23,y);
	}


	return 0;
}