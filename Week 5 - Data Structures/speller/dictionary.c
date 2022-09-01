// Implements a dictionary's functionality
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <strings.h>
#include <stdbool.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Choose number of buckets in hash table
const unsigned int N = 1000;

// Hash table
node *table[N];

// Total word in dictionary
int totalWord = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Obtain the location of the word in hash table by using hash function
    int location = hash(word);
    node *curr = table[location];

    while (curr != NULL)
    {
        // Compare the strings that are case-insensitive
        if (strcasecmp(word, curr->word) == 0)
        {
            return true;
        }

        curr = curr->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    long value = 0;
    int n = strlen(word);

    // Reference: https://www.journaldev.com/35238/hash-table-in-c-plus-plus
    // Hash the word by adding all the ASCII value of the strings in uppercase
    for (int i = 0; i < n; i++)
    {
        value += toupper(word[0]);
    }

    return value % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    int location = 0;
    char word[LENGTH + 1];
    FILE *file = fopen(dictionary, "r");

    if (file == NULL)
    {
        printf("%s cannot be opened\n", dictionary);
        return false;
    }

    while (fscanf(file, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));

        if (n == NULL)
        {
            printf("Not enough memory\n");
            return false;
        }

        // Copy the word into the new node created
        strcpy(n->word, word);
        location = hash(word);

        // Insert node at the front of linked list
        n->next = table[location];
        table[location] = n;
        totalWord += 1;
    }

    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return totalWord;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    node *curr = NULL;
    node *temp = NULL;

    // Free all the memory allocated in the hash table
    for (int i = 0; i < N; i++)
    {
        curr = table[i];
        temp = curr;

        while (curr != NULL)
        {
            curr = temp->next;
            free(temp);
            temp = curr;
        }
    }

    return true;
}
