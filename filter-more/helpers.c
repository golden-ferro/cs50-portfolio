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

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    int Gx[3][3] =
    {
        {-1, 0, 1},
        {-2, 0, 2},
        {-1, 0, 1}
    };

    int Gy[3][3] =
    {
        {-1, -2, -1},
        { 0,  0,  0},
        { 1,  2,  1}
    };

    for (int i = 0; i < height; i++)
    {
        for (int c = 0; c < width; c++)
        {
            int bx = 0;
            int gx = 0;
            int rx = 0;
            int by = 0;
            int gy = 0;
            int ry = 0;
            int bf = 0;
            int gf = 0;
            int rf = 0;
            for (int di = -1; di <= 1; di++)
            {
                for (int dc = -1; dc <= 1; dc++)
                {
                    int ni = i + di;
                    int nc = c + dc;
                    if (ni >= 0 && ni < height && nc >= 0 && nc < width)
                    {
                        bx += image[ni][nc].rgbtBlue * Gx[di + 1][dc + 1];
                        gx += image[ni][nc].rgbtGreen * Gx[di + 1][dc + 1];
                        rx += image[ni][nc].rgbtRed * Gx[di + 1][dc + 1];
                        by += image[ni][nc].rgbtBlue * Gy[di + 1][dc + 1];
                        gy += image[ni][nc].rgbtGreen * Gy[di + 1][dc + 1];
                        ry += image[ni][nc].rgbtRed * Gy[di + 1][dc + 1];
                    }
                }
            }
            bf = round(sqrt(bx * bx + by * by));
            if (bf > 255)
            {
                bf = 255;
            }
            gf = round(sqrt(gx * gx + gy * gy));
            if (gf > 255)
            {
                gf = 255;
            }
            rf = round(sqrt(rx * rx + ry * ry));
            if (rf > 255)
            {
                rf = 255;
            }
            copy[i][c].rgbtBlue = bf;
            copy[i][c].rgbtGreen = gf;
            copy[i][c].rgbtRed = rf;
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
