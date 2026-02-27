#include<stdio.h>
int main()
{
    int i,j;
    i =1;
    do{
        j=1;
        do{
            printf("%d",i);
            printf("\n");
            j++;
        }while(j<=i);
        i++;
    }while(i<=5);
    return 0;
}