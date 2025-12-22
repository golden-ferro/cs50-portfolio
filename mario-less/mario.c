#include <stdio.h>
#include <cs50.h>

int main (void)
{
    int h;
    do
    {
        h = get_int("height = ");
    }
    while (h < 1);

    int c = 0;
    int line = 0;
    while (line < h)
    {
        while (c <= line)
        {
            printf("#");
            c++;
        }
        printf("\n");
        line++;
        c = 0;

    }

}
