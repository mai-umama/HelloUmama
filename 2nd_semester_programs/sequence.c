//3 9 27 81 243 729
#include<stdio.h>
int main()
{
    int n;
    printf("enter :");
    scanf("%d",&n);
    int num =3;
    printf("sequence : ");
    for(int i =1; i<=n;i++){
        printf("%d ",num);
        num = num*3;
    }
    return 0;
}