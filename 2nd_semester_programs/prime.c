#include<stdio.h>
int main()
{
    for(int i =1;i<=50;i++){
        if(i==1){
            continue;
        }
        if(i%2==0 || i%3==0){
            continue;
        }
        if(i%5==0){
            continue;
        }
        if(i%11==0 || i%13==0){
            continue;
        }
        if(i%17==0){
            continue;
        }
        printf("%d\n",i);
    }
    return 0;
}