#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

int count_letter (char text[]);
int count_word (char text[]);
int count_sentence (char text[]);

int main (void)
{
    float L = 0;
    float S = 0;
    string text = get_string("text: ");

    L = ((float)count_letter(text) / count_word(text) * 100);
    S = ((float)count_sentence(text) / count_word(text) * 100);

    double index = 0.0588 * L - 0.296 * S - 15.8;

    float decimal_part = index - (int)index; //rounding
    int rounded_index;
    if (decimal_part >= 0.5)
    {
        rounded_index = (int)index + 1;
    }
    else
    {
        rounded_index = (int)index;
    }

    if (rounded_index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (rounded_index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", rounded_index);
    }

}

int count_sentence (char text[])
{
    int i = 0;
    int n = 0;
    while(text[i] != '\0')
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            n++;
        }
        i++;
    }
    return n;
}


int count_word (char text[])
{
    int i = 0;
    int n = 0;
    while(text[i] != '\0')
    {
        if (isspace(text[i]) > 0)
        {
            n++;
        }
        i++;
    }
    n++;
    return n;
}

int count_letter (char text[])
{
    int i = 0;
    int n = 0;
    while(text[i] != '\0')
    {
        if (isalpha(text[i]) > 0)
        {
            n++;
        }
        i++;
    }
    return n;
}
