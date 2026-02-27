#include<stdio.h>
#include<string.h>
struct student{
    int roll;
    float gpa;
    char name[100];
};
int main()
{
    struct student s1;
    s1.roll = 100;
    s1.gpa = 3.89;
    strcpy(s1.name , "umama");
    printf("Roll %d\n",s1.roll );
    printf("gpa %.2f\n", s1.gpa);
    printf("name %s", s1.name);
    return 0;
}