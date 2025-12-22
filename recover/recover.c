#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Uso: %s imagem_de_entrada\n", argv[0]);
        return 1;
    }

    char *infile = argv[1];

    FILE *inptr = fopen(infile, "rb");
    if (inptr == NULL)
    {
        fprintf(stderr, "Não foi possível abrir %s\n", infile);
        return 2;
    }

    typedef uint8_t BYTE;
    BYTE buffer[512];

    FILE *outptr = NULL;
    int file_count = 0;
    char filename[8];

    while (fread(buffer, sizeof(BYTE), 512, inptr) == 512)
    {
        int is_jpeg_start = (buffer[0] == 0xff &&
                             buffer[1] == 0xd8 &&
                             buffer[2] == 0xff &&
                             (buffer[3] & 0xf0) == 0xe0);

        if (is_jpeg_start)
        {
            if (outptr != NULL)
            {
                fclose(outptr);
                outptr = NULL;
            }

            snprintf(filename, sizeof(filename), "%03d.jpg", file_count);
            outptr = fopen(filename, "wb");
            if (outptr == NULL)
            {
                fprintf(stderr, "Erro ao criar %s\n", filename);
                fclose(inptr);
                return 3;
            }

            file_count++;
            fwrite(buffer, sizeof(BYTE), 512, outptr);
        }
        else
        {
            if (outptr != NULL)
            {
                fwrite(buffer, sizeof(BYTE), 512, outptr);
            }

        }
    }

    size_t last_read = fread(buffer, sizeof(BYTE), 512, inptr);
    if (last_read > 0 && outptr != NULL)
    {
        fwrite(buffer, sizeof(BYTE), last_read, outptr);
    }

    if (outptr != NULL)
    {
        fclose(outptr);
    }
    fclose(inptr);

    return 0;
}
