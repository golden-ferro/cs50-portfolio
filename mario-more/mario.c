#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int h;

    do
    {
        h = get_int("height: ");
    }
    while (h < 1);

    int hl = 0;
    int d = 1;
    for (int line = 0; line < h; line++)
    {
       for (hl = 0; hl < (h - d); hl++)
       {
            printf(" ");
       }
       for (hl = 0; hl < d; hl++)
       {
            printf("#");
       }
        printf("  ");
       for (hl = 0; hl < d; hl++)
       {
            printf("#");
       }
       d++;
       printf("\n");
    }
}
