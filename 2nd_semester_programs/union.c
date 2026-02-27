#include<stdio.h>
#include<string.h>
union student{
    long long int roll;
    float GPA;
    char name[200];
};
int main()
{
  union student s;
  s.roll = 2357;
  printf("roll = %lld\n", s.roll);
  s.GPA = 5.00;
  printf("gpa = %.2f\n", s.GPA);
 // strcpy(s.name,"MAISH OSMAN UMAMA");

    return 0;
}