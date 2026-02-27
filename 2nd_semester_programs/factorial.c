#include<stdio.h>
int factorial(int n){
    if(n ==0){
        //printf("No factorial");
        return 1;
    }
    else{
        return n*factorial(n-1);
    }
}
int main()
{
    int num =5;
    int result = factorial(num);
    printf("the factorial of %d is %d", num, result);
    return 0;
}