#include <stdio.h>

int main(){
    //변수 선언
	char buf[100001];
	int pipe = 0;
	int stack = 0;

    //괄호 입력
    scanf("%s", &buf[0]);

    //pipe 개수 구하는 반복문 
    //입력 받은 buf 길이 만큼 반복
	for(int i = 0; i < sizeof(buf) / sizeof(char); i++){
        //괄호가 아니면 break;
		if(buf[i] != '(' && buf[i] != ')') break;
		
		if(buf[i] == '(') pipe++;
		
		else{
			pipe--;
			
            // () 레이저이면 stack에 pipe 개수 더하기
			if(buf[i-1] == '(') stack += pipe;
			else stack++;
		}
	}
	printf("%d", stack);
}
