#include<stdio.h>
void square(int n){
    int i, j;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("* ");
        }
        printf("\n");
    }
}
int main()
{
    int side;
    printf("enter the side = ");
    scanf("%d",&side);
    square(side);
    return 0;
}