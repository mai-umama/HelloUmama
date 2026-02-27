#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i;
    int *ptr =(int*)malloc(2*sizeof(int));
    if(ptr == NULL){
        printf("memory not allocated");
        return 0;
    }
    printf("Enter two numbers:");
    for(i = 0; i<2;i++){
        scanf("%d", &ptr[i]);//(ptr +i) is also valid
    }
    ptr = (int*)realloc(ptr,4*sizeof(int));
    if(ptr == NULL){
        printf("memory not allocated");
        return 0;
    }
    printf("Enter two more numbers: ");
    for(i = 2;i<4;i++){
        scanf("%d", &ptr[i]);
    }
    for(i = 0;i<4;i++){
        printf("%d ", *(ptr+i));//ptr[i] is also valid
    }
    free(ptr);
    return 0;
}