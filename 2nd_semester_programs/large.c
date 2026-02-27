#include <stdio.h>

/* Function prototype */
//int large_num(int arr[], int size);

int large_num(int arr[])
{
    int large_arr = arr[0];

    for (int i = 1; i < 6; i++)
    {
        if (large_arr < arr[i])
        {
            large_arr = arr[i];
        }
    }
    return large_arr;
}

int main()
{
    int arr[6] = {10, 20, 30, 70, 50, 8};

    int result = large_num(arr);
    printf("the largest = %d", result);

    return 0;
}
