#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#define BLOCK_SIZE 512

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
    else
    {
        int counter = 0;
        char filename[8];
        BYTE buffer[BLOCK_SIZE];
        FILE *img = NULL;
        FILE *file = fopen(argv[1], "r");

        if (file == NULL)
        {
            printf("%s cannot be opened for reading\n", argv[1]);
            return 1;
        }

        while (fread(buffer, sizeof(BYTE), BLOCK_SIZE, file) == BLOCK_SIZE)
        {
            // Check for the first 4 bytes of jpg file in the buffer
            if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0))
            {
                // For second jpg file onwards, close the previous jpg file
                if (counter != 0)
                {
                    fclose(img);
                }

                // Create a new jpg file
                sprintf(filename, "%03i.jpg", counter);
                counter += 1;

                // Open the new jpg file
                img = fopen(filename, "w");
                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, img);
            }
            else
            {
                // Continue writing to the jpg file if already found one
                if (counter > 0)
                {
                    fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, img);
                }
            }
        }

        // Close files
        fclose(img);
        fclose(file);
        return 0;
    }
}