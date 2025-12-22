#include <stdio.h>
#include <cs50.h>
#include <string.h>

int score_calculus (char word[]);
int main (void)
{
    int s1 = 0;
    int s2 = 0;

    string w1 = get_string("Player 1: ");
    string w2 = get_string("Player 2: ");

    s1 = score_calculus (w1);
    s2 = score_calculus (w2);

    if (s1 > s2)
    {
        printf("Player 1 wins\n");
    }
    else if (s2 > s1)
    {
        printf("Player 2 wins\n");
    }
    else
    {
        printf("Tie!\n");
    }
}
int score_calculus (char word[])
    {
        int const points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
        int n = strlen(word);
        int score = 0;

        for (int i = 0; i < n; i++)
        {
            if (word[i] > 90)
            {
                word[i] -= 32;
            }
            if (word[i] >= 'A' && word[i] <= 'Z')
            {
                score += (points[word[i] - 'A']);
            }
        }
        return score;
    }
