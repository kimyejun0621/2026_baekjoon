#include <stdio.h>
#include <time.h>

int main(){
    time_t timer;
    struct tm *t;

    timer = time(NULL);
    timer += 9 * 60 * 60 ;
    t = gmtime(&timer);
    printf("%04d-%02d-%02d\n", t->tm_year +1900, t->tm_mon +1, t->tm_mday);
    return 0;
}

#include <stdio.h>
int main(){
    printf("\\    /\\");
    printf(")  ( ')");
    printf("(  /  )");
    printf(" \\(__)|");
    return 0;
}