#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    int letters = 0;
    int sentences = 0;
    int words = 0;
    int index = 0;
    float L = 0;
    float S = 0;

    // Prompt the user for input
    string text = get_string("Text: ");

    // Calculating letters
    letters = count_letters(text);

    // Calculating words
    words = count_words(text);

    // Calculating sentences
    sentences = count_sentences(text);

    // Coleman-Liau index
    L = (float) letters / (float) words * 100.0;
    S = (float) sentences / (float) words * 100.0;
    index = round(0.0588 * L - 0.296 * S - 15.8);

    // Print Grades
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", (int) index);
    }
}

int count_letters(string text)
{
    int letters = 0;
    int n = strlen(text);

    // Calculating letters
    for (int i = 0; i < n; i++)
    {
        if ((tolower(text[i]) >= 'a' && tolower(text[i]) <= 'z'))
        {
            letters += 1;
        }
    }

    return letters;
}

int count_words(string text)
{
    int words = 1;
    int n = strlen(text);

    // Calculating words
    for (int i = 0; i < n; i++)
    {
        if (text[i] == ' ')
        {
            words += 1;
        }
    }

    return words;
}

int count_sentences(string text)
{
    int sentences = 0;
    int n = strlen(text);

    // Calculating sentences
    for (int i = 0; i < n; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences += 1;
        }
    }

    return sentences;
}