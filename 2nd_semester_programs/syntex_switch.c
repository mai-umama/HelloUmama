#include<stdio.h>
int main()
{
    char grade;
    printf("enter the grade: ");
    scanf("%c",&grade);
    switch(grade){
        case'A':
        printf("excellent");
        break;
        case 'B':
        printf("Good");
        break;
        case 'C':
        printf("not bad");
        break;
        default:
        printf("failed");
    }
    return 0;
}