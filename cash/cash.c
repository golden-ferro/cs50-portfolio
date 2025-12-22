#include <stdio.h>
#include <cs50.h>

int main (void)
{
    int m;
    do
    {
        m = get_int("money: ");
    }
    while(m < 0);

    int c = 0;
    while(m > 0)
    {
        while(m - 25 >= 0)
        {
            m = m - 25;
            c++;
        }
        while(m - 10 >= 0)
        {
            m = m - 10;
            c++;
        }
        while(m - 5 >= 0)
        {
            m = m - 5;
            c++;
        }
        while(m - 1 >= 0)
        {
            m = m -1;
            c++;
        }
    }
    printf("%i\n",c);

}
