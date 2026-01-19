#include <stdio.h>
int main(){
    int students[31] = {0};

    //28명 입력하기
    for(int i = 0; i < 28; i++){
        int num = 0;
        scanf("%d", &num);
        students[num] = 1;
    }

    for(int i = 1; i < 31; i++){
        if(students[i] == 0){
            printf("%d\n", i);
        }
    }

    return 0;
}