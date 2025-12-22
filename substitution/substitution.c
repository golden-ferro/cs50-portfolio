#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

bool valid_key(string key, int c);
string encipher(string key, string plaintext);
int main (int argc,string argv[])
{
    if (valid_key(argv[1], argc) == 0)
    {
        printf("Usage: ./substitution key(must contain 26 caracters)\n");
        return 1;
    }
    string plaintext = get_string("plaintext: ");
    string ciphertext1 = encipher (argv[1], plaintext);
    printf("ciphertext: %s\n", ciphertext1);

}

string encipher(string key, string plaintext)
{
    int len = strlen(plaintext);
    char *ciphertext = malloc(len); // Usa a mesma memória do plaintext

    for (int i = 0; i < len; i++)
    {
        if (islower(plaintext[i]))
        {
            int p = plaintext[i] - 'a';
            ciphertext[i] = tolower(key[p]); // Mantém minúsculas
        }
        else if (isupper(plaintext[i]))
        {
            int p = plaintext[i] - 'A';
            ciphertext[i] = toupper(key[p]); // Mantém maiúsculas
        }
        else
        {
            ciphertext[i] = plaintext[i]; // Mantém caracteres não alfabéticos
        }
    }

    return ciphertext;
}

bool valid_key(string key, int c)
{
    if (c != 2)
    {
        return 0;
    }

    if (strlen(key) != 26)
    {
        return 0; // Retorna 0 em vez de false
    }

    int marked[26] = {0}; // Inicializa todas as posições com 0

    for (int i = 0; i < 26; i++)
    {
        if (isalpha(key[i]) == 0) // Verifica se a chave contém apenas letras
        {
            return 0; // Retorna 0 em vez de false
        }

        int p = tolower(key[i]) - 'a'; // Converte a letra para um índice de 0 a 25

        if (marked[p] > 0) // Se a letra já apareceu, a chave é inválida
        {
            return 0;
        }

        marked[p] = 1; // Marca a letra como vista (incrementando)
    }

    return 1; // Retorna 1 em vez de true
}
