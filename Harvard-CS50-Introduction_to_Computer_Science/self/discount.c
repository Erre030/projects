#include <cs50.h>
#include <stdio.h>

float discount (float humpty, int percentage);


int main(void)
{
    float regular = get_float("Regular Price: ");
    int percent_off = get_int("Percent Off: ");

    //The types used for the function are already correctly named and assigned for sale = discount(...).
    //The discount function already knows which data types it should process, so the names of the influencing function parameters are irrelevant and only the types are important.
    //To create coherence, you select suitable/speaking variables such as price & Co..
    //If another float were to be added now, it would have to be placed in the correct position in the function listing depending on the intended use.
    //Example: float sale = discount(regular, percent_off, float damaged);
    //In the function, the float should then be included at the desired position or in the correct order/when it should be used.

    float sale = discount(regular, percent_off);
    printf("Sale Price: %.2f\n", sale);
}

float discount (float humpty, int percentage)
{
    return humpty * (100 - percentage) / 100;
}
