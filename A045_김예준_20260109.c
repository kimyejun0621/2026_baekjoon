//1. 알파벳 대소문자들을 입력받는다. 
//2. 알파벳들의 개수를 센다. 
//2-1. 알파벳들의 개수는 어떻게 새야할까? 
// 2-2. 기존에 있는 흠,, 
//3. 가장 많은 개수의 대문자를 출력한다. 

#define ALP_SIZE 26

#include <stdio.h>
#include <string.h>
#include <ctype.h>

char word[1000000];
int count[ALP_SIZE] = {0};

int main(){
    scanf("%s",word);
    for(int i = 0; word[i] != '\0'; i++){

        int index = toupper(word[i]) - 'A';
        count[index]++;
        
    }

    int max_count = 0;
    char answer = 0;
    for(int j = 0; j < ALP_SIZE; j++){

        if(count[j] > max_count){
            max_count = count[j];
            answer = j + 'A';
        }
        
        else if(count[j] == max_count){
            answer = '?';
        }

    }

    printf("%c",answer);

}