#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];
   // int*p;
    int *p = arr;
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    printf("print ");
    // for(int i=0;i<n;i++){
    //     printf("%d ",arr[i]);
    // }
    for(int i=0;i<n;i++){
        printf("%d ",*(p+i));
    }
    return 0;
}