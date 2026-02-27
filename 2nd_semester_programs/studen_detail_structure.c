#include<stdio.h>
#include<string.h>
struct student{
    int ID;
    char Name[50];
    float Marks;
};
int main()
{
    int n;
    printf("enter the number of students: ");
    scanf("%d",&n);
    struct student st[n];
    for(int i = 0;i<n;i++){
        printf("Enter the detail of the students : \n");
        printf("ID: ");
        scanf("%d",&st[i].ID);
        char tempName[50];
        printf("Name: ");
        scanf("%s",tempName);
        strcpy(st[i].Name,tempName);

        printf("Marks: ");
        scanf("%f",&st[i].Marks);

    }
    printf("The detail of the students\nId\tName\tMarks\n");
    for(int i =0;i<n;i++){
        printf("%d\t%s\t%.2f\n",st[i].ID,st[i].Name,st[i].Marks);
    }
    return 0;
}