#include<stdio.h>
int main()
{
    int x=1, y=2;
    if(x&y){
        printf("result is one");
    }
    else if(x&&y){
        printf("result is 1");
    }
    return 0;
}