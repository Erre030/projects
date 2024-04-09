#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates // Kandidatennamen werden eingegeben
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}










// Update vote totals given a new vote
bool vote(string name)
{
    //go through array of candidate names(candidate_count) which holds the number of candidates
    for (int i = 0; i < candidate_count; i++)
    {
        //compare if vote is name unsinf stringcompare
        if (strcmp(name, candidates[i].name) == 0)
        {
            candidates[i].votes ++;
            return true;
        }

    }
    return false;

}

// Print the winner (or winners) of the election
void print_winner()
{
    //function can get any value form main by referring to the value in the function.
    //function doesnt need a parameter, only if there is an specific input requierd to get the result. If function takes no parameter, it doesnt give parameter back.
    int max_votes = 0;

    //go through list of candidates and get hte maximum votes
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > max_votes)
        {
            max_votes = candidates[i].votes;
        }
    }

    //print out all candidates with the max vote
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == max_votes)
        {
            printf("%s\n", candidates[i].name);
        }
    }

}