#include<stdio.h>
#include<stdlib.h>
int main()
{
    int *p;
    p = (int *)malloc(sizeof(int));
    if(p==NULL){
        printf("not allocated");
        return 1;
    }
    *p =10;
    printf("%d",*p);
    return 0;
}