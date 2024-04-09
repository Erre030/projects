#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height, row, column, spaces, spacebetween;

    do
    {
        height = get_int("Height:");
    }
    while (height < 1 || height > 8);


//for rows
    for (row = 0 ; row < height ; row++)
    {
//for spaces before 1st pyramid
        for (spaces = 0 ; spaces < height - row - 1 ; spaces++)
        {
            printf(" ");
        }

//1st pyramid columns
        for (column = 0 ; column <= row ; column++)
        {
            printf("#");
        }

//space between pyramids
        for (spacebetween = height - 1; spacebetween <= height ; spacebetween++)
        {
            printf(" ");
        }

//2nd pyramid columns
        for (column = 0 ; column <= row ; column++)
        {
            printf("#");
        }

        printf("\n");
    }

}
