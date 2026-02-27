#include<stdio.h>
int main()
{
    int n=10;
    if(n>0){
        goto positive;
    }
    else{
        goto negetive;
    }
    printf("this will not be printed\n");// the compiler direct go to te next parts cause of goto statement
    positive:
    printf("this number is positive\n");
    goto end;
    negetive:
    printf("this number is negetive\n");
    goto end;
    end:
    printf("end the program\n");
    return 0;
}