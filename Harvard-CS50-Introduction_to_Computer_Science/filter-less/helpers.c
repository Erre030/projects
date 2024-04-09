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
//every pixel is checked for its RGB-values (two-dimensional-array) and gets transformed by nested loops. The following applies to each pixel.
//1.call pixel and create average of RGB-values --> set all RGB-parameter on average-values (grayscale).
//2. if average no int --> round onto nearest int.

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepiaBlue = round(image[i][j].rgbtRed * .272 + image[i][j].rgbtGreen * .534 + image[i][j].rgbtBlue * .131);
            int sepiaRed = round(image[i][j].rgbtRed * .393 + image[i][j].rgbtGreen * .769 + image[i][j].rgbtBlue * .189);
            int sepiaGreen = round(image[i][j].rgbtRed * .349 + image[i][j].rgbtGreen * .686 + image[i][j].rgbtBlue * .168);

            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }

            image[i][j].rgbtBlue = sepiaBlue;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtRed = sepiaRed;


        }
    }
}
//compute sepia-values by sepia formular --> round --> if not between 0-255 = max./min.).

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
    {
        int n = width - 1;

        for (int j = 0; j < (width / 2); j++)
            // int abbreviates automatically after comma, numbers with decimal values are automatically shorten to ints (e.g.: 49 / 2 = 24.5 >> 24).
        {

            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][n];
            image[i][n] = temp;
            n--;
        }
    }


}
//mirror pixel in the individual lines


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
//average values of a pixel of all pixel who tpuch this pixel (3x3).
//lesser pixel at edges

//procedure: 1. duplicate array --> 2. determine pixel average values --> 2a. round value to int. --> 3. set value of 2a. as pixel value  
// (choose the duplicated copy array with the original values for the original color values and alter the pixel in the image array

//comments:
//>a.create duplicate, if you have to alter the values of something but need the original values as reference.
//>b.correct position of elements in loops important.
//>c.set values to 0 before reusing the method/algorithm
//>d.if statement say that choosen pixel can only be included in the array, if it lies in the width and height (inside the actual picture).
//>d1.First the pixel algorithm is used to get a selection, then the specific pixel which belon to the raster/picture are added. 
