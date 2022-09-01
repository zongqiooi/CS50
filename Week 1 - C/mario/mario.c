#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height = 0;

    // Get the height of pyramind
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // For each row of pyramind
    for (int i = 0; i < height; i++)
    {
        // For each column of pyramid
        for (int j = 0; j < (height + 1) * 2; j++)
        {
            // Print left spaces
            if (j < height - i - 1)
            {
                printf(" ");
            }
            // Print left hashes
            else if (j >= height - i - 1 && j < height)
            {
                printf("#");
            }
            // Print gap
            else if (j == height || j == height + 1)
            {
                printf(" ");
            }
            // Print right hashes
            else if (j > height + 1 && j < ((height + 1) * 2) - height + i + 1)
            {
                printf("#");
            }
        }

        printf("\n");
    }
}