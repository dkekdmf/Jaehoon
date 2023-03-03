#include <stdio.h>
#pragma warning(disable:4996)
#define SIZE 100
typedef struct StackType {

	int arr[100]; // int형 데이터 100개
	int top;
} StackType;

void init(StackType* s) {
	s->top = -1; // 배열은 index 0부터 시작
}
//empty : return 1
//!empty : return 0;
int is_empty(StackType* s) {

	if (s->top == -1)
		return 1;
	return 0;
}
//full : return1
//!full : return 0
int is_full(StackType* s) {

	if(s->top == SIZE -1)
		return 1;
	return 0;
}
void push(StackType* s, int value) 
{
	if (is_full(s))
	{
		printf("Stack is full");
		exit(1);
	}
	printf("\npushed %d\n", value);
	s->arr[++(s->top)] = value;
}
int pop(StackType* s) {
	if (is_empty(s))
	{
		printf("\nStack is empty\n");
		exit(1);
	}
	return s->arr[(s->top)--];
}
int peek(StackType* s) {
	if (is_empty(s)) {
		printf("Stack is empty");
	}
	return s->arr[(s->top)];
}
int main(void) {

	StackType s;
	init(&s); //stack 초기화됨.

	push(&s,3);
	push(&s,2);
	push(&s,1);

	printf("\npeek : %d\n", peek(&s));
	printf("\npop : %d\n", pop(&s));
	printf("\npop : %d\n", pop(&s));

	printf("\npop : %d\n", pop(&s));
	return 0;
}