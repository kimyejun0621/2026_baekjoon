#include <stdio.h>

int factorial(int n){
    if(n == 0){
        return 1;
    }
    return n * factorial(n-1);
}

int main(){
    int ans = 0;
    int num = 0;

    scanf("%d",&num);

    ans = factorial(num);

    printf("%d",ans);
    
    return 0;
}