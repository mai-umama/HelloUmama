#include<stdio.h>
#include<string.h>
struct bloodDonation{
    char Paitent_name[100];
    char location[100];
    char date[100];
};
int main()
{
    int n;
    printf("Enter the number of paitent : ");
    scanf("%d",&n);
    struct bloodDonation donor[n];
    FILE *file;
    file = fopen("E:\\HelloUmama\\Blood_donor.txt","w");
    if(file == NULL){
        printf("file not created!");
        return 1;
    }
    printf("enter the donor details: ");
    for(int i =0;i<n;i++){
       printf("Paitent Name : ");
       char tempname[100];
       scanf("%s",tempname);
       strcpy(donor[i].Paitent_name,tempname);
       printf("Location : ");
       char templocation[100];
       scanf("%s",templocation);
       strcpy(donor[i].location,templocation); 
       printf("Date : ");
       char tempdate[100];
       scanf("%s",tempdate);
       strcpy(donor[i].date,tempdate); 
    }
    fprintf(file, "Name %s\tLocation%s\tDate%s\n",donor->Paitent_name,donor->location,donor->date);
    fclose(file);
    printf("Done");
    return 0;
}