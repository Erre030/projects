#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height, row, column, spaces;

    do
    {
        height = get_int("Height:");
    }
    while (height < 1 || height > 8);


//for rows
    for (row = 0 ; row < height ; row++)
    {
//for spaces
        for (spaces = 0 ; spaces < height - row - 1 ; spaces++)
        {
            printf(" ");
        }

//for columns
        for (column = 0 ; column <= row ; column++)
        {
            printf("#");
        }

        printf("\n");
    }

}