#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    //Here the individual ranks are carried out for each voter. You then don't have the individual voters (you don't need them), but the individual ranks.
    //The nested loop is used to create a two-dimensional array voter[1][jwlg. rank] for each voter

    //ranks[] is used for each voter individually: 1. loop through each voter 2.create ranks[].!!!
    //3. check vote cast (vote) /second for-loop --> 4. preferences are created for this one voter --> 5. procedure starts from the beginning !!!

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}
















// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i], name) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }
    // TODO
    return false;

//comments
//1a. index of the candidate is equated with rank. Candidate is linked to the respective rank by index. individual voters are not treated in this function.
//1b.name is not necessary because the candidate is stored on a specific index in the candidates [] array.
//1c. ranks [i] was already assigned in the previous definition, now each ranks[i] receives a [j] in preferences[i][j]

//description
//1.the function receives the arguments rank, name and ranks. If name matches the name of a valid candidate,
//1a.you should update the ranks array to indicate that the voter has the candidate as their rank preference (where 0 is the first preference, 1 is the second preference, etc.)
//2.remember that ranks[i] here represents the i-th preference of the user. > rank[i] is equated with the respective candidate for the rank
//3.the function should return true if the rank was successfully captured, and false otherwise (e.g. if name is not the name of one of the candidates).
//4.you can assume that no two candidates will have the same name.

//the array ranks[] is created for each voter and contains the preferences for each voter > then the preferences of the individual voters are sorted and combined into pairs in preferences

}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            preferences[ranks[i]][ranks[j]]++;
        }
    }
    // TODO
    return;

//comments
//With a two-dimensional array, the first nested loop uses the second column of the array, the second the third, and so on.
//Here, nested loops are transferred to the preferences array. The ranks for the individual voters have already been entered in main, now the preferences must be sorted.
//ranks[i] and ranks[j] refer to the candidate index
//!!! ranks[] is used for each voter individually: 1. loop through each voter 2.create ranks[]. !!!
//!!! 3. check vote cast (vote) /second for loop 4. preferences are created for this one voter 5. procedure starts from the beginning !!!
//Always check for which volume the data is used / which sequence is created (e.g. all voters in an array or an array for each voter individually)

//description
//1.the function is called once for each voter and receives as argument the array ranks (remember that ranks[i] is the i-th preference of the voter, where ranks[0] is the first preference).
//2.the function should update the global preferences array to add the preferences of the current voter.
//2a.Recall that preferences[i][j] should represent the number of voters who prefer candidate i to candidate j.
//3. you can assume that each voter will rank each of the candidates.

}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    pair_count = 0;

    for (int i = 0; i < candidate_count - 1; i++) //because last candidate is automatically captured by j, otherwise there is segmentation fault
    {
        for (int j = i + 1; j < candidate_count; j++)
            {
                if (preferences[i][j] > preferences[j][i])
                {
                    pairs[pair_count].winner = i;
                    pairs[pair_count].loser = j;
                    pair_count++;
                }

                if (preferences[j][i] > preferences[i][j])
                {
                    pairs[pair_count].winner = j;
                    pairs[pair_count].loser = i;
                    pair_count++;
                }

            }
    }
    // TODO
    return;


//description:
//1. The function should include all candidate pairs in which a candidate is preferred in the pairs array.
//1a. A candidate pair where one candidate is not preferred should not be included in the array.
//2.the function should update the global variable pair_count so that it indicates the number of candidate pairs.
//2a.(The pairs should therefore all be stored between pairs[0] and pairs[pair_count - 1], inclusive).

//comments:
//The available ranking of the candidates is taken as the starting point (rank[0] to rank[2], e.g. Alice [0], bob [1], charlie [2])
// if a rank(i) has more/less preferences than another(j), it is sorted into pairs array(here it is counted whether there is a preference that was formed in the last function).
// It is ignored if the numbers are the same.
//pair_count assigns the pair to the current number of the pair_count. The next number in the pair_count is then selected and assigned with ++
//!!! You can also just assign numbers to numbers. This is more cryptic but in the end more data-saving and efficient (e.g. preferences on pair_count)!!!
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{

for (int i = 0; i < pair_count; i++) // nested loops for access to both columns of the array
{
    int max = i;
   int strength = preferences [pairs[i].winner][pairs[i].loser] - preferences [pairs[i].loser][pairs[i].winner];

   for(int j = i+1; j < pair_count; j++)
   {
    int next_strength = preferences [pairs[j].winner][pairs[j].loser] - preferences [pairs[j].loser][pairs[j].winner];

   if (next_strength > strength) //Comparison of the margins of the candidates' winnings
   {
    max = j; //Index of the pair_count that is the highest
    strength = next_strength;
    }
   }
    if (max != i) //if the index has changed, then...
    {
pair temp = pairs[i];
pairs[i] = pairs[max];
pairs[max] = temp;
    }


}
return;

}

//comments:
//1. the values from which differences are to be formed, which are then to be sorted, are in the preferences array, so this must be accessed
//2. the nested loop only considers the first element of the array, the second is unimportant )
//2a. wouldn't pairs[i].winner - pairs[i]. loser also be possible? > probably not, because you have to take the values from the preferences array.
//3. the different arrays or variables simply indicate what is being searched/where the data is being pulled from and do not have to be the same
//results:
//Check formulations/ where does data come from and what do I need ? need the position of the preference and in pair_count each preference has a position.
//>The pairs are stored in pairs, i.e. they are ordered
//Note the order again. Also data origin


    // TODO

//description:
//1. the function should sort the pairs in decreasing order of probability of victory, where the probability of victory is defined as the number of voters,
//1a.that favor the preferred candidate. If several pairs have the same probability of winning, you can assume that the order does not matter.


// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // TODO
    return;

//1.the function should create the initial locked graph by adding all edges in decreasing order of victory strength as long as the edge does not generate a cycle.

}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    return;

//1.the function should output the name of the candidate that is the source of the graphic. You can assume that there is no more than one source.

}

//Additional functions are permitted
