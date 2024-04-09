// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>
#include <strings.h>


#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = (LENGTH * 'z');

// Hash table
node *table[N];






// Returns true if word is in dictionary, else false
bool check(const char *word)
//==NULL Conditions removed, because logically there are only buckets that have been created and therefore none with NULL
{
    int index = hash(word);

    node *cursor = table[index];

    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}





// Hashes word to a number
unsigned int hash(const char *word)
//at math ( all letter values together with math, each word has an individual value and gets its own bucket, later the values can then be compared in the check function)
{
    int total_sum = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        total_sum += tolower(word[i]);

    }
    return (total_sum); // %N is not necessary, as N cannot be exceeded by its definition (LENGTH * 'z').

}





int total_words = 0;
// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{

    //open file
    FILE *file = fopen(dictionary, "r");

    //check if valid
    if (file == NULL)
    {

        printf("file invalid");
        return false;
    }
    //copy strings
    char word [LENGTH + 1];
    while (fscanf(file, "%s", word) != EOF)
        //changed from do while loop --> with do while the loop runs through once and the condition is only checked for the first time at the end.
    {
        //fscanf(from where?, what?, where to?)
        //(only free what you have malloced yourself. >> does not have to be freed. Mostly just the edit (close at the end, freen, etc.)
        //(what you have written yourself, the rest is usually done by the compiler/language itself)
        //(always use the same place in the memory and transfer the word afterwards to make room for a new word, according to my understanding automatically by fscanf)

//create new node
        node *n = malloc(sizeof(node));
        if (n == NULL) // if there is no more memory from Malloc, then n(node) no longer receives a new address
        {
            return false;
        }
        strcpy(n->word, word);
        n->next = NULL; //Arrow moves to subclass and inserts the respective information there. (n has two subclasses >> word >> next)
        //load node into hashtable
        int index = hash(word);
        if (table[index] == NULL)
        {
            table[index] = n;
        }
        else
        {
            n-> next = table[index]; // new nodes points at the first of the list
            table[index] = n; // head of linked list becomes new node
        }
        total_words++;
    }
    fclose(file);
    return true;
}





// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return total_words;
}




// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor;
            //tmp must be set to cursor not to table[i]:
            //Within the while loop, the tmp is then updated with the current cursor value so that the current node can be freed and the same table[i] element is not constantly freed until cursor == NULL
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;
}


