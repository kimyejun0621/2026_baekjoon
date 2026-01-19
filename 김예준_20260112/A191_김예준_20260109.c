#include <stdio.h>
int main(){
    int count;
    scanf("%d", &count);

    for(int i = 0; i < count; i++){
        int num1, num2 ;
        scanf("%d %d",&num1, &num2);
        printf("%d\n", num1 + num2);
    }

    return 0;
}