#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

bool only_fdigit (int input1,string input2[]); //check if main returns only a number, return 0 or 1.
char rotate (char t, int key); //rotates the letter.

int main (int argc,string argv[])
{
    bool tf = only_fdigit (argc, argv);
    if (tf)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int key = atoi(argv[1]);

    string plaintext = get_string("plaintext:  ");
    int size = strlen(plaintext);
    printf("ciphertext: ");
    for (int i = 0; i < size; i++)
    {
        char l = plaintext[i];
        if (isalpha(l))
        {
            char rl = rotate(l, key);
            printf("%c", rl);
        }
        else
        {
            printf("%c", l);
        }
    }
    printf("\n");
    return 0;
}

char rotate (char t, int key)
{
     // for lowercase letters
    if (islower(t))
    {
        // position of letters
        char letters[26];
        for (int i = 0; i < 26; i++)
        {
            letters[i] = 'a' + i;
        }

        // t position
        int p = t - 'a';

        // rotate t
        int r = (p + key) % 26;
        return letters[r];
    }
    else // for capital letters
    {
        // position of letters
        char letters[26];
        for (int i = 0; i < 26; i++)
        {
            letters[i] = 'A' + i;
        }

        // t position
        int p = t - 'A';

        // rotate t
        int r = (p + key) % 26;
        return letters[r];
    }
}

bool only_fdigit (int input1,string input2[])
{
    if (input1 != 2)
    {
        return 1;
    }

    for(int n = 0; n < strlen(input2[1]); n++)
    {
        if (isdigit(input2[1][n]) == 0)
        {
            return 1;
        }
    }
    return 0;
}
