#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>


int main(int argc, string argv[])
{

// check for correct argument amount
    if (argc != 2)
    {
        printf("Error1\n");
        return 1;
    }

// proof if digit
    for (int i = 0 ; i < strlen(argv[1]); i++)
    {
        //if no digit
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

//change type string to int
    int k = atoi(argv[1]);

//get plaintext + prepare ciphertext so result is printed afterwards
    string plaintext = get_string("plaintext:  ");
    printf("Ciphertext: ");

//use key on plaintext. Loop over lower case/upper (mod %26), else no letter (just print)
    for (int j = 0; j < strlen(plaintext); j++)
    {
//if upper
        if (isupper(plaintext[j]))
        {
            printf("%c", (plaintext[j] - 65 + k) % 26 + 65);
//if lower
        }
        else if (islower(plaintext[j]))
        {
            printf("%c", (plaintext[j] - 97 + k) % 26 + 97);
        }
//no letter
        else
        {
            printf("%c", plaintext[j]);
        }
    }
    printf("\n");
    return 0;
}
