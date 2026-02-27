#include<stdio.h>
#include<stdlib.h>
int main()
{
    int *ptr;
    int n =5;

    ptr = (int*)calloc(n,sizeof(int));
    if(ptr == NULL){
        printf("Memory not allocated");
        return 0;
    }
    for(int i =0;i<n;i++){
        printf("%d ",ptr[i]);
    }
    
    return 0;
}