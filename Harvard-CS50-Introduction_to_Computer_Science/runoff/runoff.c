#include <cs50.h>
#include <stdio.h>
#include <string.h>


// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates > ist array von Kandidaten mit den drei obigen Werten aus typedef struct
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

















//1.Realisierung der einzelnen Elemente
//2.Zeitliche Verknüpfung der einzelnen Elemente



// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    //1.Es wird durch das Array candidate.count[i] durchiteriert, da es alle  Kandidatennamen enthält.
    //1a.Stimmt der eingegebene Kandidatenname(name) mit dem Namen eines Kandidaten überein (candidates[i].name > beinhaltet die erstellte Datenstruktur candidate und seine Unterklassen(name,votes,eliminated)
    //1b.wird er mit der Präferenz des Wählers gleichgesetzt (preferences[voter][rank] = i) und es wird true zurückgegeben
    //2.so wird die Präferenz mit dem jeweiligen Kandidaten verknüpft bzw. auf sie übertragen (beide haben nun den gleichen Wert)
    //3.andernfalls wird false zurückgegeben


    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
        {

            preferences[voter][rank] = i;
            return true;
        }
    }
    return false;

}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    //darstellung der Stimmen, die jeder Kandidat momentan hat
    //dabei wählt jeder Wähler seine top-Präferenz , if not eliminated


    //1a.der erste for loop geht durch die Wähleranzahl. Der zweite Loop legt fest, das für jeden Wähler alle Kandidaten durchgespielt werden
    //1b.wenn der Kandidat nicht elimiert ist, wird eine Stimme zu seinem Konto hinzugefügt. Danach wird der Loop unterbrochen, damit die weiteren Präferenz nicht aus gezählt werden
    //1c.ein Szenario dafür zu bauen, dass der User eliminated ist ist nicht nötig, da der Loop automatisch nur Kandidaten anwählt, die noch nicht eliminiert sind

    //Learnings:
    //es ist möglich array in array zu stacken
    //preferences[i][j] steht hier stellvertretend für candidates[i] aus der vorherigen Funktion, in welcher diese gleichgesetzt wurden

    for (int i = 0; i < voter_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (candidates[preferences[i][j]].eliminated == false)
            {
                candidates[preferences[i][j]].votes ++;
                break;
            }
        }
    }

    //Hinweise: voter_count beinhaltet die Nummer von Wählern. Für jeden Wähler muss ein Wahlzettel mit Präferenzen erstellt werden
    //Präferenzen für den Wähler [i] werden repräsentiert durch preferences[i][0] für erste Präferenz, etc.
    // die candidate struct hat einen Bereich für eliminated. Dieser wird true, wenn Kandidat eleminiert ist(bool)
    //die candidate struct enthält die votes welche nach jeder eliminierung angepasst/geupdated werden müssen
    // wenn der gewünschte Kandidat vom Wahlzetelle des Wählers vorhanden, nicht eleminiert ist, sollte danach nichts mehr abgerufen werden. Mit break kann aus dem loop ausgestiegen/er für später pausiert werden

}







// Print the winner of the election, if there is one
bool print_winner(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > voter_count / 2)
        {
            printf("%s\n", candidates[i].name);
            return true;
        }
    }

    //wenn ein Kandidat mehr als die Hälfte der Stimmen hat, sollte sein Name geprintet werden und true ausgegeben werden
    //wenn noch niemand gewonnen hat, dann sollte false ausgegeben werden

    //Hinweise: voter_count beinhaltet die Anzahl von Wählern. Auf dieser Basis wird die Anzahl für die Hälfte der Stimmen gebildet (voter_count /2 +1)

    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    //wenn int min votes = vote_counter ist es möglich direkt mit dem ersten Wert zu arbeiten ( wenn der Gesamtwert als ausgang genommen wird und dann mit einem Teilwert ersetzt wird)
    int min = voter_count;

    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].eliminated == false && candidates[i].votes < min)
        {
            min = candidates[i].votes;


            //Nicht möglich > wahrscheinlich segmentation fault (Zugriff auf nicht vorhandenen Memory für diesen Abschnitt)
            //if(candidates[i].votes < candidates[i+1].votes)
            //{
            //min = candidates[i].votes;
            //}
        }

    }

    //die minimale Stimmenanzahl für jeden Kandidaten, der noch nicht eleminiert ist sollte ausgegeben werden

    //Hinweise: Durch die candidaten loopen und den Kandidaten finden, der noch im Rennen ist und die wenigsten Stimmen hat. Dafür werden folgende Parameter gebraucht : Anzahl Stimmen, eliminated: false

    // TODO
    return min;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    int same = 0;
    int remaining = 0;

    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].eliminated == false)
        {
            remaining++;
        }
        if (candidates[i].votes == min)
            //hier nicht nochmal auf eliminated false checken, weil nur die allgemeine Anzahl zählt, nicht die genauen Kandidaten
        {
            same++;
        }
    }

    if (same == remaining)
    {
        return true;
    }
    //die Funktion nimmt ein Argument min ( kommt von find_min) , die geringste  Stimmenanzahl, die irgendjemand in der Wahl momentan hat
    //wenn alle kandidaten die gleiche stimmenanzahl habe sollte die Funktion true lauten, anssonsten false

    //Hinweise: Ein Unentschieden ist möglich, wenn jeder Kandidat der noch nicht eliminiert ist die gleiche Anzahl an Stimmen hat. Wenn also min bei allen Kandidaten gleich ist , ist es ein Unentschieden.

    // TODO
    else
    {
        return false;
    }
}
// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == min)
        {
            candidates[i].eliminated = true;
        }
    }
    //nimmt auch das Argument min(Minimale Anzahl an Stimmen für Kandidaten)
    //Der Kandidat mit der niedrigsten Stimmanzahl sollte eliminiert werden

    // TODO
}