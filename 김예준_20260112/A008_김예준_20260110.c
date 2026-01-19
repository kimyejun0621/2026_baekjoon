#include <stdio.h>
//5개 문자열을 받는다? 
#define MAX_STUDENTS 1000

int main(){

    int C = 0;
    int num_students = 0;
    scanf("%d",&C);

    for(int i = 0; i < C; i++){

        int scores[MAX_STUDENTS];
        double result = 0;
        double avg = 0;
        int sum = 0;
        int above_avg_count = 0;
        

        scanf("%d", &num_students);

        for(int j = 0; j < num_students; j++){
            scanf("%d", &scores[j]);
            sum += scores[j];
        }

        avg = (double)sum / num_students;

        for(int k = 0; k < num_students; k++){
            if(scores[k] > avg){
                above_avg_count +=1;
            }
        }

        result = ((double)above_avg_count / num_students) *100;
        printf("%.3f%%\n",result);

    }
    return 0;
}