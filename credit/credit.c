#include <stdio.h>
#include <cs50.h>

int main (void)
{
    long x = get_long("credit card number: ");

    int sum = 0;
    int c = 1;
    long long z = x;
    int cl = 0;

    while (x != 0)
    {
        int r = x % 10;
        x = x / 10;

        if (c % 2 == 0)
        {
            r = r * 2;
            if (r > 9)
            {
                r = (r % 10) + (r / 10);
            }
        }
        sum = sum + r;
        c++;
        cl++;
    }
    if (sum % 10 == 0)
    {
        while (z >= 100)
        {
            z /= 10;
        }
        if ((z == 34 || z == 37) && (cl == 15))
        {
            printf("AMEX\n");
        }
        else if ((z >= 51 && z <= 55) && (cl == 16))
        {
            printf("MASTERCARD\n");
        }
        else if ((z / 10 == 4 || z == 4) && (cl == 13 || cl == 16))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
