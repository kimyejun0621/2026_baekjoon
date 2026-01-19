#include <stdio.h>
#include <stdlib.h>
#define SIZE 100005
//compare 공식
int compare(const void *a, const void *b){
    int num1 = *(int *)a;
    int num2 = *(int *)b;

    if(num1 < num2)return -1;
    if(num1 > num2)return 1;
    return 0;
}

//이분탐색구현 공부(업,다운 게임 방식)
int Bsearch(int arr[],int val, int n){
    int start = 0;
    int end = n - 1;
    int mid;
    while(start <= end){
        mid = (start + end) / 2;
        if(arr[mid] == val){
            return 1;
        }
        else if (arr[mid] < val){
            start = mid + 1;
        }
        else{
            end = mid - 1;
        }
    }
    return 0;
}

int main(){

    int N[SIZE];
    int N_count = 0;
    scanf("%d", &N_count);
    for(int i = 0; i < N_count; i++){
        scanf("%d",&N[i]);
    }

    qsort(N, N_count, sizeof(int), compare);

    int M_count = 0;
    int temp;
    scanf("%d", &M_count);
    for(int i = 0; i < M_count; i++){
        scanf("%d", &temp);
        printf("%d\n",Bsearch(N,temp,N_count));
    }
    return 0;
}