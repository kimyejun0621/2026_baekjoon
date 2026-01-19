#include <stdio.h>
int main(){

    int count;
    scanf("%d",&count);

    int num[count];
    
    for(int i = 0; i < count; i++){
        scanf("%d", &num[i]);
    }

    int find;
    int check = 0;
    scanf("%d", &find);
    for(int i = 0; i < count; i++){
        if(find == num[i]){
            check ++ ;
        }
    }
    printf("%d", check);

    return 0;
}