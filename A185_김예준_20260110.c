#include <stdio.h>
int main(){
    int num1, num2;
    scanf("%d %d", &num1, &num2);

    if(num1 > num2){
        printf(">");
    }
    else if(num2 > num1){
        printf("<");
    }
    else{
        printf("==");
    }
    return 0;
}