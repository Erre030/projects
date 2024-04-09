#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>





int main(int argc, string argv[])
{

// check for correct argument amount
    if (argc != 2)
    {
        printf("Error1\n");
        return 1;
    }

//check for single letters
    //first for-loop looks at each element in the key.
    //Second nested for-loop compares this element to every element following, starting at the next element
    //when elements are the same = error

    string key = argv[1];

    for (int i = 0; i < strlen(key); i++)
    {
        for (int j = i + 1; j < strlen(key); j++)
        {
            if (toupper(key[i]) == toupper(key[j]))
            {
                printf("Error2\n");
                return 1;
            }

        }
    }

//check for lengths and alphabetic

    for (int i = 0, n = strlen(key); i < n; i++)
    {
        if (n != 26 || !isalpha(key[i]))
        {
            printf("Error3\n");
            return 1;
        }

    }
    printf("\n");


    string plaintext = get_string("plaintext:  ");


//easier handling with the key, bc key upper/lowercase doesn't matter

    for (int i = 0; i < strlen(key); i++)
    {
        if (islower(key[i]))
        {
            key[i] = key[i] - 32;
        }
    }

    printf("ciphertext: ");

//get the individual ciphertext
    //get the value of the particular letter by substract the different values after asci chart (65/97)
    //fill in the letter value to indicate the needed position of the key and print the key position
    //if the letter is lower case adding +32 is needed, bc the key was converted into uppercase before by -32
    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (isupper(plaintext[i]))
        {
            int letter_value = plaintext[i] - 65;
            printf("%c", key[letter_value]);
        }
        else if (islower(plaintext[i]))
        {
            int letter_value = plaintext[i] - 97;
            printf("%c", key[letter_value] + 32);
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
    return 0;

}