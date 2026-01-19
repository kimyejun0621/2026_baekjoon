// //1. 입력받을 문장의 개수를 입력받는다.
// //2. 입력받은 문장에서 하나하나를 살펴본다. 만약 O라면 점수를 1추가, 그전에도O이라면 +1추가함.? 
#include <stdio.h>
#include <string.h>

//기존코드1
// int main(){
//     int len = 0;
//     char ox[81];
//     int sum = 0;
//     int add = 0;
//     scanf("%d",&len);
//     for(int i = 0; i < len; i++){
//         scanf("%s",ox);
//         for(int i = 0; i < strlen(ox); i++){
//             if(ox[i] == 'O'){
//                 add +=1;
//                 sum += add;
//             }
//             else{
//                 add = 0;
//             }
//         }
//         printf("%d\n", sum);
//         sum = 0;
//         add = 0;
//     }
// }

//수정코드 
#define SIZE 81
int main(){
    int count = 0;
    char ox[SIZE];

    int sum = 0;
    int combo = 0;

    scanf("%d", &count);

    for(int i = 0; i < count; i++){
        scanf("%s",ox);
        int len = strlen(ox);

        sum = 0;
        combo = 0;

        for(int j = 0; j < len; j++){
            if(ox[j] == 'O'){
                combo +=1;
                sum += combo;
            }

            else{
                combo = 0;
            }

        }
        printf("%d\n",sum);

    }
    return 0;
}