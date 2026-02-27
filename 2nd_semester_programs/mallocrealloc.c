#include<stdio.h>
#include<stdlib.h>
int main()
{
    int n;
    printf("enter the size of the array= ");
    scanf("%d",&n);
    int *arr = (int *)malloc(n*sizeof(int));
    // for(int i =0;i<n;i++){
    //     //arr[i]= i+1;
    //     scanf("%d",&arr[i]);
    // }
    for(int i =0;i<n;i++){
        printf("%d ", arr[i]);
    }
    printf("Enter new size of memory = ");
    scanf("%d",&n);
    arr = (int *)realloc(arr,n*sizeof(int));
    // for(int i =0;i<n;i++){
    //     //arr[i]= i+1; 
    //     //scanf("%d",&arr[i]);
    // }
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
        }
    free(arr);
    return 0;
}