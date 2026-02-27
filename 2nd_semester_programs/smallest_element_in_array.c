#include<stdio.h>
int main()
{
    int n;
    printf("enter the number of element : ");
    scanf("%d",&n);
    int arr[n];
    int *ptr = arr;
    //arr[0]
    printf("enter the elements: ");
    for(int i =0;i<n;i++){
        scanf("%d",&ptr[i]);
    }
    int smallest_element = ptr[0];
    for(int  j=0;j<n;j++){
        if(ptr[j]<smallest_element){
            smallest_element = ptr[j];
        }
        //printf("%d",smallest_element);
    }
    printf("%d",smallest_element);
    return 0;
}