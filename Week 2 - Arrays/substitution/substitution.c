#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        // Error: Not enough command line arguments
        printf("Usage: ./substitution key\n");
        return 1;
    }
    else
    {
        if (strlen(argv[1]) != 26)
        {
            // Error: Key too short
            printf("Key must contain 26 characters.\n");
            return 1;
        }

        for (int i = 0; i < 26; i++)
        {
            // Check for digits in keys
            if (isdigit((argv[1])[i]) != 0)
            {
                printf("Key must only contain characters.\n");
                return 1;
            }

            // Check for duplicates in keys 
            for (int j = 0; j < 26; j++)
            {
                if (i != j && (argv[1])[i] == (argv[1])[j])
                {
                    printf("Key must not contain duplicates.\n");
                    return 1;
                }
            }
        }

        string plaintext = get_string("plaintext:  ");
        string map = argv[1];
        int n = strlen(plaintext);

        for (int i = 0; i < n; i++)
        {
            // For lowercase
            if (plaintext[i] >= 'a' && plaintext[i] <= 'z')
            {
                plaintext[i] = tolower(map[plaintext[i] - 'a']);
            }

            // For uppercase
            if (plaintext[i] >= 'A' && plaintext[i] <= 'Z')
            {
                plaintext[i] = toupper(map[plaintext[i] - 'A']);
            }
        }

        printf("ciphertext: %s\n", plaintext);
        return 0;
    }
}