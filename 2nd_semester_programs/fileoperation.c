#include<stdio.h>

int main()
{
    FILE *fptr;
    char str[50];

    fptr = fopen("E:\\HelloUmama\\rownak.txt","w");   // write mode

    if(fptr == NULL){
        printf("File cannot be opened");
        return 1;
    }

    fprintf(fptr, "this is a text.\n");

    printf("Enter a string: ");
    fgets(str,50,stdin);

    fprintf(fptr,"this is written : %s",str);

    fclose(fptr);

    return 0;
}
