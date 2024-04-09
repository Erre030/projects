#include "helpers.h"
#include <math.h>


// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int average = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }

}


// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        int n = width - 1;

        for (int j = 0; j < (width / 2); j++)
            // int automattically shortes after comma, so (e.g. 49 / 2 = 24.5 >> 24).
        {

            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][n];
            image[i][n] = temp;
            n--;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++) //step one
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];

        }
    }
    float totalred = 0;
    float totalgreen = 0;
    float totalblue = 0;
    int counter = 0;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            for (int rowconfg = i - 1; rowconfg <= i + 1; rowconfg++)
            {
                for (int colconfg = j - 1; colconfg <= j + 1; colconfg++)
                {
                    if (colconfg < width && rowconfg < height && colconfg >= 0 && rowconfg >= 0)
                    {
                        totalred += copy[rowconfg][colconfg].rgbtRed;
                        totalgreen += copy[rowconfg][colconfg].rgbtGreen;
                        totalblue += copy[rowconfg][colconfg].rgbtBlue;
                        counter++;
                    }

                }
            }
            image[i][j].rgbtRed = round(totalred / counter);
            image[i][j].rgbtGreen = round(totalgreen / counter);
            image[i][j].rgbtBlue = round(totalblue / counter);
            counter = 0;
            totalred = 0;
            totalgreen = 0;
            totalblue = 0;
        }
    }
}












// Detect edges

void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];

        }
    }

    int Gx [3][3] =
    {
        {-1, 0, 1},
        {-2, 0, 2},
        {-1, 0, 1}
    };

    int Gy [3][3] =
    {
        {-1, -2, -1},
        {0, 0, 0},
        {1, 2, 1}
    };


    //makes accessing single pixels possible / loops through single pixels.
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //is defined as 9er-matrix for a 3x3 grid similar as for blur --> doesn't need own loops, cause depends on single pixel which are looped already.
            int rows[3] = {i - 1, i, i + 1};
            int colums[3] = {j - 1, j, j + 1};

            int gxred, gxgreen, gxblue;
            gxred = gxgreen = gxblue = 0;

            int gyred, gygreen, gyblue;
            gyred = gygreen = gyblue = 0;

            //loop through rows & colums and through gx/gy ( rows / colums addresses pixel values of previous loops (linked to them) (i,j).
            for (int row = 0; row < 3; row++)
            {
                for (int col = 0; col < 3; col++)
                {
                    //new row-values, cause both matrices are 3x3.
                    int pixrow = rows [row];
                    int pixcol = colums [col];

                    //create pixel which is selected.
                    RGBTRIPLE pixel = copy[pixrow][pixcol];

                    //new values get included if they stay in the array --> has to lie in (gx/gy) and (rows / colums) --> grid (blur-like) functions as base.
                    if (pixrow < width && pixcol < height && pixrow >= 0 && pixcol >= 0)
                        //entire grid must be able to be mapped so that values are included.
                    {

                        //multiplication of the Gx and Gy elements with the respective pixel values from the 9 grid (blur-like).
                        gxred += pixel.rgbtRed * Gx[row][col];
                        gxgreen += pixel.rgbtGreen * Gx[row][col];
                        gxblue += pixel.rgbtBlue * Gx[row][col];

                        gyred += pixel.rgbtRed * Gy[row][col];
                        gygreen += pixel.rgbtGreen * Gy[row][col];
                        gyblue += pixel.rgbtBlue * Gy[row][col];
                    }
                }
            }

            //compute values for new pixels.
            int newred = round(sqrt(gxred * gxred + gyred * gyred));
            int newgreen = round(sqrt(gxgreen * gxgreen + gygreen * gygreen));
            int newblue = round(sqrt(gxblue * gxblue + gyblue * gyblue));

            if (newred > 255)
            {
                newred = 255;
            }
            if (newgreen > 255)
            {
                newgreen = 255;
            }
            if (newblue > 255)
            {
                newblue = 255;
            }

            //insert new values.
            image[i][j].rgbtRed = newred;
            image[i][j].rgbtGreen = newgreen;
            image[i][j].rgbtBlue = newblue;

        }
    }


}
