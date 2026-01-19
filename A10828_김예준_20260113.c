#include <stdio.h>
#include <string.h>

#define MAX_SIZE 100005

int stack[MAX_SIZE];
int top = -1;

void push(int data){
    stack[++top] = data;
}

int pop(){
    if(top == -1){
        return -1;
    }
    return stack[top--];
}

int empty(){
    if(top == -1){
        return 1;
    }
    return 0;
}

int get_top(){
    if(top == -1){
        return -1;
    }
    return stack[top];
}

int size(){
    return top + 1;
}

