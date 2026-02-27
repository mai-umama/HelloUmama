#include<stdio.h>
#include<string.h>
struct employee{
    int id;
    char dob[15];
    char position[1000];
};

int main()
{
    int n;
    printf("enter the number of employee= ");
    scanf("%d", &n);
    struct employee e[n];
    for(int i =0;i<n;i++){
        printf("\n--emoloyee--%d\n", i+1);
        printf("enter id =");
        scanf("%d",&e[i].id );
        printf("enter the dob= ");
        scanf("%s",e[i].dob);
        printf("enter the position = ");
        scanf("%s",e[i].position);
    }
    printf("--Employee details ---\n");
    for(int j= 0; j<n;j++){
        printf("--Employee--%d\n", j+1);
    printf("Employee ID = %d\n", e[j].id);
    printf("Date of Birth = %s\n", e[j].dob);
    printf("Position = %s\n", e[j].position);}

    
    return 0;
}