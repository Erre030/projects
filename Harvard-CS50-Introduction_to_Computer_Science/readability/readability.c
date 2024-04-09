#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>


int count_letters();
int count_words();
int count_sent();


int main(void)
{

//string of user for sourcecode

    string text = get_string("Text: ");


//count letters

//return value must always be collected as a variable of the function and has to have the same type
    int letters = count_letters(text);

//count words
    int words = count_words(text);

//count sentences
    int sent = count_sent(text);

//compute level of difficulty with cleman-Liau formula

    float L = (float) letters /  words * 100;
    float S = (float) sent / words * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);


//Output Grade: ... specific level of difficulty / below 1:  1 > Before Grade 1 / over 16: 16  > Grade 16+

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }


}

//(string func_text) specifies how the value assigned to the function in main is saved for the function. The name in the function is independent of the name (text) specified in main
int count_letters(string func_text)
{
    int letter_counter = 0;
    for (int i = 0; i < strlen(func_text) ; i++)
    {
        if (isalpha(func_text[i]))
        {
            letter_counter++;
        }
    }
    return letter_counter;
//code after return is not run (dead code)
}

int count_words(string func_text)
{
    int word_counter = 0;
    for (int i = 0; i < strlen(func_text) ; i++)
    {
        if (func_text[i] == 32)
        {
            word_counter++;
        }
    }
    return word_counter + 1;
}

int count_sent(string func_text)
{
    int sent_counter = 0;
    for (int i = 0; i < strlen(func_text) ; i++)
    {
        if (func_text[i] == 33 || func_text[i] == 46  || func_text[i] == 63)
        {
            sent_counter++;
        }
    }
    return sent_counter;
}



