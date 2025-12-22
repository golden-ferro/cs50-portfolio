#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int c = 0; c < width; c++)
        {
            int b = image[i][c].rgbtBlue;
            int g = image[i][c].rgbtGreen;
            int r = image[i][c].rgbtRed;
            int m = round((b + g + r) / 3.0);
            image[i][c].rgbtBlue = m;
            image[i][c].rgbtGreen = m;
            image[i][c].rgbtRed = m;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int c = 0; c < width; c++)
        {
            int b = image[i][c].rgbtBlue;
            int g = image[i][c].rgbtGreen;
            int r = image[i][c].rgbtRed;
            int sr = round(0.393 * r + 0.769 * g + 0.189 * b);
            int sg = round(0.349 * r + 0.686 * g + 0.168 * b);
            int sb = round(0.272 * r + 0.534 * g + 0.131 * b);
            if (sr > 255)
            {
                sr = 255;
            }
            if (sg > 255)
            {
                sg = 255;
            }
            if (sb > 255)
            {
                sb = 255;
            }
            image[i][c].rgbtBlue = sb;
            image[i][c].rgbtGreen = sg;
            image[i][c].rgbtRed = sr;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int c = 0; c < width / 2; c++)
        {
            int b = image[i][c].rgbtBlue;
            int g = image[i][c].rgbtGreen;
            int r = image[i][c].rgbtRed;
            image[i][c].rgbtBlue = image[i][width - (c + 1)].rgbtBlue;
            image[i][c].rgbtGreen = image[i][width - (c + 1)].rgbtGreen;
            image[i][c].rgbtRed = image[i][width - (c + 1)].rgbtRed;
            image[i][width - (c + 1)].rgbtBlue = b;
            image[i][width - (c + 1)].rgbtGreen = g;
            image[i][width - (c + 1)].rgbtRed = r;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int c = 0; c < width; c++)
        {
            int counter = 0;
            int b = 0;
            int g = 0;
            int r = 0;
            for (int di = -1; di <= 1; di++)
            {
                for (int dc = -1; dc <= 1; dc++)
                {
                    int ni = i + di;
                    int nc = c + dc;
                    if (ni >= 0 && ni < height && nc >= 0 && nc < width)
                    {
                        b += image[ni][nc].rgbtBlue;
                        g += image[ni][nc].rgbtGreen;
                        r += image[ni][nc].rgbtRed;
                        counter++;
                    }
                }
            }
            copy[i][c].rgbtBlue = round((float)b / counter);
            copy[i][c].rgbtGreen = round((float)g / counter);
            copy[i][c].rgbtRed = round((float)r / counter);
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int c = 0; c < width; c++)
        {
            image[i][c] = copy[i][c];
        }
    }
    return;
}
